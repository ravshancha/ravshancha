// Stand-in for the Apps Script web app, for trying site/api/lead.php on this machine without a spreadsheet
// (see "Lokal sinash" in README.md). Like Google, it answers the POST with a redirect to a page that holds
// the JSON result, and it prints every lead it receives.
// Usage: node tools/leads/mock-sheets.js [port] [fail]   → http://localhost:8775/exec; "fail" rejects every lead.
const http = require("http");

const PORT = Number(process.argv[2] || 8775);
const FAIL = process.argv[3] === "fail";
const SECRET = "local-test-secret";
const results = new Map();
let row = 1;

http.createServer((req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);
  if (req.method === "GET" && url.pathname === "/echo") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(results.get(url.searchParams.get("id")) || JSON.stringify({ ok: false, error: "unknown" }));
    return;
  }
  let body = "";
  req.on("data", (chunk) => { body += chunk; });
  req.on("end", () => {
    let lead = null;
    try { lead = JSON.parse(body); } catch (error) { lead = null; }
    const accepted = !FAIL && lead && lead.secret === SECRET;
    if (accepted) row += 1;
    const { secret, ...shown } = lead || {};
    console.log(`\n${req.method} ${url.pathname} → ${accepted ? `row ${row}` : "rejected"}\n${JSON.stringify(shown, null, 2)}`);
    const id = String(results.size + 1);
    results.set(id, JSON.stringify(accepted ? { ok: true, row, mailed: true } : { ok: false, error: FAIL ? "sheet" : "secret" }));
    res.writeHead(302, { Location: `/echo?id=${id}` });
    res.end();
  });
}).listen(PORT, "127.0.0.1", () => console.log(`mock leads web app on http://localhost:${PORT}/exec — secret "${SECRET}"${FAIL ? " (rejects every lead)" : ""}`));
