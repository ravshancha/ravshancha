# cPanel deployment

The website is stored in `site/` on the `development` branch. GitHub Actions deploys that directory to cPanel automatically after every website push to `development`.

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

## Flow

1. Push a website change to `development` (anything under `site/`, or the workflow file itself).
2. GitHub Actions checks out the repository.
3. The contents of `site/` are synchronized to the configured cPanel directory over FTPS. Files removed from `site/` are removed on the server too. A running deploy is never cancelled by a newer push; the newer push waits for it.

Actions are pinned to commit SHAs; the version is noted in a comment next to each `uses:` line.

## Server rules

`site/.htaccess` is deployed with the site. It redirects `http://` and `www.` to `https://ravshancha.uz`, sets browser caching (images 30 days, HTML 10 minutes), registers AVIF/WebP MIME types and blocks public access to `.ftp-deploy-sync-state.json`, the file the deploy action keeps on the server to remember what it uploaded. Do not delete that file manually; the next deploy would re-upload everything.

The `main` branch contains only the repository README and does not trigger deployment.
