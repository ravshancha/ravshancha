// Local preview of the whole site/ folder: the CV site at / and the selling site at /business/
// (static files only — api/lead.php does not run here, so the form shows its Telegram fallback).
// Usage: node tools/business/serve.js [port]   → http://localhost:8772/business/
const http = require("http");
const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "..", "..", "site");
const PORT = Number(process.argv[2] || process.env.PORT || 8772);
const TYPES = {
  ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript", ".json": "application/json",
  ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".webp": "image/webp", ".avif": "image/avif",
  ".ico": "image/x-icon", ".txt": "text/plain; charset=utf-8", ".xml": "application/xml"
};

http.createServer((req, res) => {
  if (req.method !== "GET" && req.method !== "HEAD") {
    res.writeHead(405, { "Content-Type": "text/plain" }).end("static preview: only GET is served");
    return;
  }
  let pathname = decodeURIComponent(req.url.split("?")[0]);
  if (pathname.endsWith("/")) pathname += "index.html";
  const file = path.join(ROOT, path.normalize(pathname));
  if (!file.startsWith(ROOT)) {
    res.writeHead(403).end("forbidden");
    return;
  }
  fs.readFile(file, (error, body) => {
    if (error) {
      res.writeHead(404, { "Content-Type": "text/plain" }).end("not found: " + pathname);
      return;
    }
    res.writeHead(200, { "Content-Type": TYPES[path.extname(file).toLowerCase()] || "application/octet-stream", "Cache-Control": "no-store" });
    res.end(req.method === "HEAD" ? undefined : body);
  });
}).listen(PORT, "127.0.0.1", () => console.log(`serving ${ROOT} on http://localhost:${PORT}`));
