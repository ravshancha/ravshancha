# cPanel deployment

The website is stored in `site/` on the `development` branch. GitHub Actions can deploy that directory to cPanel automatically after every website push to `development`.

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

1. Push a website change to `development`.
2. GitHub Actions checks out the repository.
3. Only the contents of `site/` are synchronized to the configured cPanel directory.

The `main` branch contains only the repository README and does not trigger deployment.
