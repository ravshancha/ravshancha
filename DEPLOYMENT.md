# cPanel deployment

The website is stored in `site/` on the `development` branch. GitHub Actions checks every website change and then deploys `site/` to cPanel.

## Workflow

`.github/workflows/deploy-cpanel.yml` runs on every push to `development` that touches `site/**`, `lighthouserc.json` or the workflow itself (and on pull requests targeting `development`):

1. **check** — validates `site/*.html` with the W3C Nu validator (`html5validator`), checks external links with `lychee` (social networks that block bots are excluded) and runs Lighthouse on the static files using `lighthouserc.json`. Lighthouse thresholds are warnings for now; tighten them to `error` once the scores are stable. The Lighthouse report is attached to the run as an artifact.
2. **deploy** — runs only after `check` succeeds, only for pushes (not pull requests) and only when the repository variable `CPANEL_DEPLOY_ENABLED` is `true`. It synchronizes the contents of `site/` to the configured cPanel directory over FTPS. Files removed from `site/` are removed on the server too.

Actions are pinned to commit SHAs; the version is noted in a comment next to each `uses:` line.

## GitHub secrets

Add these repository secrets under **Settings → Secrets and variables → Actions → Secrets**:

- `CPANEL_FTP_SERVER` — FTP hostname, for example `ftp.example.com`
- `CPANEL_FTP_USERNAME` — cPanel FTP account username
- `CPANEL_FTP_PASSWORD` — cPanel FTP account password

## GitHub variables

Add these under **Settings → Secrets and variables → Actions → Variables**:

- `CPANEL_DEPLOY_ENABLED` — set to `true` after all connection details are ready
- `CPANEL_FTP_SERVER_DIR` — remote directory such as `/public_html/` or `./`
- `CPANEL_FTP_PROTOCOL` — `ftps` by default; use `ftp` only if encrypted FTP is unavailable
- `CPANEL_FTP_PORT` — `21` by default

The deploy job remains safely skipped until `CPANEL_DEPLOY_ENABLED` is set to `true`.

## Server rules

`site/.htaccess` is deployed with the site. It redirects `http://` and `www.` to `https://ravshancha.uz`, sets browser caching (images 30 days, HTML 10 minutes), registers AVIF/WebP MIME types and blocks public access to `.ftp-deploy-sync-state.json`, the file the deploy action keeps on the server to remember what it uploaded. Do not delete that file manually; the next deploy would re-upload everything.

The `main` branch contains only the repository README and does not trigger deployment.
