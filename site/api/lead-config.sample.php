<?php
// Reference only: the real lead-config.php is written on every deploy from the repository secrets and
// variables (LEAD_SHEETS_URL, LEAD_SHEETS_SECRET, LEAD_NOTIFY_EMAIL, LEAD_MAIL_FROM — see DEPLOYMENT.md),
// so a copy edited by hand on the server is overwritten by the next deploy.
// lead-config.php must never be committed: the repository is public and these values are secrets.
// Step-by-step setup of the spreadsheet and its script: tools/leads/README.md
return [
    // Web app address of the Apps Script bound to the leads spreadsheet (ends with /exec).
    'sheets_url' => '',
    // The same random string as SECRET in the script (Code.gs).
    'sheets_secret' => '',
    // Optional backup: if the sheet cannot be reached, the request is e-mailed here straight from the server.
    'notify_email' => '',
    // Optional sender of that backup e-mail; by default noreply@<this host>.
    // 'mail_from' => 'noreply@ravshancha.uz',
];
