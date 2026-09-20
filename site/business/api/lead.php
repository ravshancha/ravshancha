<?php
// Lead endpoint: takes the diagnostic request from the site form and forwards it to Telegram.
// The bot token and chat id live in lead-config.php on the server only (see lead-config.sample.php);
// that file is never committed. Any answer other than {"ok":true} makes the page fall back to
// the visitor's own Telegram, so a lead is not lost while this endpoint is unconfigured.
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

function respond(int $status, array $body): void
{
    http_response_code($status);
    echo json_encode($body, JSON_UNESCAPED_UNICODE);
    exit;
}

function text_length(string $value): int
{
    return function_exists('mb_strlen') ? mb_strlen($value, 'UTF-8') : strlen($value);
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    respond(405, ['ok' => false, 'error' => 'method']);
}

// A JSON content type forces a CORS preflight for cross-site scripts, and no CORS headers are sent here.
if (stripos($_SERVER['CONTENT_TYPE'] ?? '', 'application/json') !== 0) {
    respond(415, ['ok' => false, 'error' => 'content_type']);
}

$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
if ($origin !== '' && parse_url($origin, PHP_URL_HOST) !== preg_replace('/:\d+$/', '', $_SERVER['HTTP_HOST'] ?? '')) {
    respond(403, ['ok' => false, 'error' => 'origin']);
}

$configFile = __DIR__ . '/lead-config.php';
if (!is_file($configFile)) {
    respond(503, ['ok' => false, 'error' => 'not_configured']);
}
$config = require $configFile;
$token = trim((string)($config['bot_token'] ?? ''));
$chatId = trim((string)($config['chat_id'] ?? ''));
if ($token === '' || $chatId === '') {
    respond(503, ['ok' => false, 'error' => 'not_configured']);
}

$raw = file_get_contents('php://input', false, null, 0, 8192);
$data = json_decode($raw === false ? '' : $raw, true);
if (!is_array($data)) {
    respond(400, ['ok' => false, 'error' => 'json']);
}

// Honeypot: people never see this field. Bots get a success answer and nothing is sent.
if (trim((string)($data['website'] ?? '')) !== '') {
    respond(200, ['ok' => true]);
}

$name = trim(preg_replace('/\s+/u', ' ', (string)($data['name'] ?? '')) ?? '');
$phone = (string)($data['phone'] ?? '');
$info = trim((string)($data['info'] ?? ''));
$lang = in_array($data['lang'] ?? '', ['uz', 'ru'], true) ? $data['lang'] : 'uz';
$page = substr(preg_replace('/[^\w\/\-.]/', '', (string)($data['page'] ?? '')) ?? '', 0, 120);

if (text_length($name) < 2 || text_length($name) > 80 || !preg_match('/^[0-9]{9}$/', $phone) || text_length($info) > 1000) {
    respond(422, ['ok' => false, 'error' => 'validation']);
}

// At most 5 requests per 10 minutes from one address. If the temp folder is not writable the limit is skipped.
$dir = sys_get_temp_dir() . '/rv-leads';
if (is_dir($dir) || @mkdir($dir, 0700, true)) {
    $file = $dir . '/' . hash('sha256', $_SERVER['REMOTE_ADDR'] ?? 'unknown') . '.json';
    $handle = @fopen($file, 'c+');
    if ($handle !== false && flock($handle, LOCK_EX)) {
        $now = time();
        $stored = json_decode((string)stream_get_contents($handle), true);
        $hits = array_values(array_filter(is_array($stored) ? $stored : [], static function ($time) use ($now) {
            return is_int($time) && $time > $now - 600;
        }));
        $limited = count($hits) >= 5;
        if (!$limited) {
            $hits[] = $now;
        }
        ftruncate($handle, 0);
        rewind($handle);
        fwrite($handle, (string)json_encode($hits));
        flock($handle, LOCK_UN);
        fclose($handle);
        if ($limited) {
            respond(429, ['ok' => false, 'error' => 'rate_limit']);
        }
    }
}

$time = (new DateTime('now', new DateTimeZone('Asia/Tashkent')))->format('Y-m-d H:i');
$lines = [
    'Yangi ariza — diagnostika',
    'Ism: ' . $name,
    'Telefon: +998' . $phone,
];
if ($info !== '') {
    $lines[] = 'Muammo: ' . $info;
}
$lines[] = 'Til: ' . $lang . ($page !== '' ? ' · Sahifa: ' . $page : '');
$lines[] = 'Vaqt: ' . $time . ' (Toshkent)';

// Plain text on purpose: no parse_mode, so nothing a visitor types is interpreted as markup.
$query = http_build_query(['chat_id' => $chatId, 'text' => implode("\n", $lines), 'disable_web_page_preview' => 'true']);
$url = 'https://api.telegram.org/bot' . $token . '/sendMessage';

$answer = false;
if (function_exists('curl_init')) {
    $curl = curl_init($url);
    curl_setopt_array($curl, [
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $query,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_CONNECTTIMEOUT => 5,
        CURLOPT_TIMEOUT => 8,
    ]);
    $answer = curl_exec($curl);
    curl_close($curl);
} else {
    $answer = @file_get_contents($url, false, stream_context_create(['http' => [
        'method' => 'POST',
        'header' => 'Content-Type: application/x-www-form-urlencoded',
        'content' => $query,
        'timeout' => 8,
        'ignore_errors' => true,
    ]]));
}

$result = is_string($answer) ? json_decode($answer, true) : null;
if (!is_array($result) || ($result['ok'] ?? false) !== true) {
    respond(502, ['ok' => false, 'error' => 'delivery']);
}

respond(200, ['ok' => true]);
