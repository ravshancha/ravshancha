// Stand-in for the Telegram Bot API, for trying api/lead.php on this machine without a real bot
// (see "Formani lokal sinash" in README.md). Prints every message lead.php sends and answers like sendMessage.
// Usage: node tools/business/mock-telegram.js [port] [fail]   → http://localhost:8774; "fail" answers with an error.
const http = require("http");

const PORT = Number(process.argv[2] || 8774);
const FAIL = process.argv[3] === "fail";

http.createServer((req, res) => {
  let body = "";
  req.on("data", (chunk) => { body += chunk; });
  req.on("end", () => {
    const fields = Object.fromEntries(new URLSearchParams(body));
    console.log(`\n${req.method} ${req.url}  chat_id=${fields.chat_id || ""}\n${fields.text || body}`);
    res.writeHead(FAIL ? 400 : 200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(FAIL ? { ok: false, error_code: 400, description: "mock failure" } : { ok: true, result: { message_id: 1 } }));
  });
}).listen(PORT, "127.0.0.1", () => console.log(`mock Telegram API on http://localhost:${PORT}${FAIL ? " (answers with an error)" : ""}`));
