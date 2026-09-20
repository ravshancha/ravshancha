<?php
// Copy this file to lead-config.php ON THE SERVER (cPanel File Manager → api/) and fill it in there.
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
