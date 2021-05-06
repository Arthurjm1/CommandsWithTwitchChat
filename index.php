<?php

require_once 'TwitchSocket.php';

$commands = [
    'left',
    'right',
    'up',
    'down',
    'a',
    'b',
    'start',
    'select'
];

$twitchChat = new TwitchSocket("USER_NICK", "USER_OAUTH_TOKEN");
$twitchChat->connect();

while (true) {
    $content = $twitchChat->read();

    $parts = explode(':', $content);
    $message = strtolower(trim($parts[2]));

    if (in_array($message, $commands) == true) {
        exec("key.py $message");
    }
}
