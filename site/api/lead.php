<?php
// Lead endpoint of the CV site: takes the "order a project" form and writes it to the leads spreadsheet
// through the Apps Script web app from tools/leads (that script also e-mails the owner about every new row).
// The web app address and its secret live in lead-config.php on the server only (see lead-config.sample.php);
// that file is never committed. If the sheet cannot be reached, the request is e-mailed straight from here
// when notify_email is set. Any answer other than {"ok":true} makes the page offer its fallback, so a lead
// is not lost while this endpoint is unconfigured.
declare(strict_types=1);

// A warning or a fatal error printed into the body would leave the page with a 200 it cannot read, so errors
// are kept out of the answer and a death before respond() is turned into a status the page can name.
ini_set('display_errors', '0');
register_shutdown_function(static function (): void {
    $error = error_get_last();
    if ($error === null || !in_array($error['type'], [E_ERROR, E_PARSE, E_CORE_ERROR, E_COMPILE_ERROR], true)) {
        return;
    }
    if (!headers_sent()) {
        http_response_code(500);
    }
    echo json_encode(['ok' => false, 'error' => 'server']);
});

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

// Posts the lead to the Apps Script web app. Google answers a POST with a redirect to the page that holds
// the script's JSON, so redirects are followed (as GET, which is what that page expects).
function save_to_sheet(string $url, string $secret, array $lead): bool
{
    $payload = json_encode(['secret' => $secret] + $lead, JSON_UNESCAPED_UNICODE);
    if ($payload === false) {
        return false;
    }
    if (function_exists('curl_init')) {
        $curl = curl_init($url);
        curl_setopt_array($curl, [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload,
            CURLOPT_HTTPHEADER => ['Content-Type: application/json'],
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_MAXREDIRS => 4,
            CURLOPT_CONNECTTIMEOUT => 5,
            CURLOPT_TIMEOUT => 12,
        ]);
        $answer = curl_exec($curl);
        curl_close($curl);
    } else {
        $answer = @file_get_contents($url, false, stream_context_create(['http' => [
            'method' => 'POST',
            'header' => 'Content-Type: application/json',
            'content' => $payload,
            'timeout' => 12,
            'ignore_errors' => true,
        ]]));
    }
    $result = is_string($answer) ? json_decode($answer, true) : null;
    return is_array($result) && ($result['ok'] ?? false) === true;
}

// Backup notification, used only when the sheet did not take the lead.
function mail_lead(string $to, string $from, array $lead): bool
{
    // Shared hosting sometimes disables mail() outright; calling it then is a fatal error, not a false.
    if (!function_exists('mail')) {
        return false;
    }
    $lines = [
        'Yangi ariza — loyiha buyurtmasi',
        'Ism: ' . $lead['name'],
        'Telefon: ' . $lead['phone'],
        'Loyiha haqida: ' . $lead['info'],
        'Til: ' . $lead['lang'] . ($lead['page'] !== '' ? ' · Sahifa: ' . $lead['page'] : ''),
        'Vaqt: ' . $lead['time'] . ' (Toshkent)',
        '',
        'Diqqat: bu ariza Google Sheets jadvaliga yozilmadi — uni jadvalga qo‘lda kiriting.',
    ];
    $subject = '=?UTF-8?B?' . base64_encode('ravshancha.uz: yangi ariza — ' . $lead['name']) . '?=';
    $headers = ['From: ' . $from, 'MIME-Version: 1.0', 'Content-Type: text/plain; charset=UTF-8', 'Content-Transfer-Encoding: 8bit'];
    return @mail($to, $subject, implode("\n", $lines), implode("\r\n", $headers));
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    respond(405, ['ok' => false, 'error' => 'method']);
}

// A JSON content type forces a CORS preflight for cross-site scripts, and no CORS headers are sent here.
if (stripos($_SERVER['CONTENT_TYPE'] ?? '', 'application/json') !== 0) {
    respond(415, ['ok' => false, 'error' => 'content_type']);
}

$host = preg_replace('/:\d+$/', '', $_SERVER['HTTP_HOST'] ?? '') ?? '';
$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
if ($origin !== '' && parse_url($origin, PHP_URL_HOST) !== $host) {
    respond(403, ['ok' => false, 'error' => 'origin']);
}

$configFile = __DIR__ . '/lead-config.php';
if (!is_file($configFile)) {
    respond(503, ['ok' => false, 'error' => 'not_configured']);
}
$config = require $configFile;
$sheetsUrl = trim((string)($config['sheets_url'] ?? ''));
$sheetsSecret = trim((string)($config['sheets_secret'] ?? ''));
$notifyEmail = trim((string)($config['notify_email'] ?? ''));
if (!preg_match('#^https?://#i', $sheetsUrl) || $sheetsSecret === '') {
    $sheetsUrl = '';
}
if (filter_var($notifyEmail, FILTER_VALIDATE_EMAIL) === false) {
    $notifyEmail = '';
}
if ($sheetsUrl === '' && $notifyEmail === '') {
    respond(503, ['ok' => false, 'error' => 'not_configured']);
}
$mailFrom = trim((string)($config['mail_from'] ?? ''));
if (filter_var($mailFrom, FILTER_VALIDATE_EMAIL) === false) {
    // The Host header comes from the visitor: only letters, digits, dots and dashes survive.
    $mailFrom = 'noreply@' . (preg_replace('/[^a-z0-9.\-]/i', '', $host) ?: 'localhost');
}

$raw = file_get_contents('php://input', false, null, 0, 8192);
$data = json_decode($raw === false ? '' : $raw, true);
if (!is_array($data)) {
    respond(400, ['ok' => false, 'error' => 'json']);
}

// Honeypot: people never see this field. Bots get a success answer and nothing is stored.
if (trim((string)($data['website'] ?? '')) !== '') {
    respond(200, ['ok' => true]);
}

$name = trim(preg_replace('/\s+/u', ' ', (string)($data['name'] ?? '')) ?? '');
$phone = (string)($data['phone'] ?? '');
$info = trim((string)($data['info'] ?? ''));
$lang = in_array($data['lang'] ?? '', ['uz', 'ru', 'en'], true) ? $data['lang'] : 'uz';
$page = substr(preg_replace('/[^\w\/\-.]/', '', (string)($data['page'] ?? '')) ?? '', 0, 120);

if (text_length($name) < 2 || text_length($name) > 80 || !preg_match('/^[0-9]{9}$/', $phone)
    || text_length($info) < 10 || text_length($info) > 1000) {
    respond(422, ['ok' => false, 'error' => 'validation']);
}

// At most 5 requests per 10 minutes from one address. If the temp folder is not writable the limit is skipped.
$dir = sys_get_temp_dir() . '/rv-leads-cv';
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

$lead = [
    'source' => 'cv',
    'name' => $name,
    'phone' => '+998' . $phone,
    'info' => $info,
    'lang' => $lang,
    'page' => $page,
    'time' => (new DateTime('now', new DateTimeZone('Asia/Tashkent')))->format('Y-m-d H:i'),
];

$saved = $sheetsUrl !== '' && save_to_sheet($sheetsUrl, $sheetsSecret, $lead);
if (!$saved && ($notifyEmail === '' || !mail_lead($notifyEmail, $mailFrom, $lead))) {
    respond(502, ['ok' => false, 'error' => 'delivery']);
}

respond(200, ['ok' => true]);
