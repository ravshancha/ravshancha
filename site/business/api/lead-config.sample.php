<?php
// Copy this file to lead-config.php ON THE SERVER (cPanel File Manager) and fill it in there.
// lead-config.php must never be committed: the repository is public and the bot token is a secret.
//
// 1. Telegram → @BotFather → /newbot → copy the token.
// 2. Open your new bot and press Start, then open
//    https://api.telegram.org/bot<TOKEN>/getUpdates — "chat":{"id": ...} is your chat id.
//    (For a group: add the bot to the group and use the group's negative id.)
return [
    'bot_token' => '',
    'chat_id' => '',
    // Optional, normally absent: another address for the Telegram Bot API — a relay when the host cannot
    // reach api.telegram.org, or a local stand-in while testing (see tools/business/README.md).
    // 'api_base' => 'https://api.telegram.org',
];
