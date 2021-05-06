# Commands With Twitch Chat

This app uses PHP sockets to allows you to send specific Windows commands through Twitch chat.

## Usage

First, change the strings "USER_NICK" and "USER_OAUTH_TOKEN" in ```index.php``` to your twitch username and oauth token, respectively.

Then, be sure to be on the app folder an run:
```
php index.php
```
Now type one of the commands specified in ```index.php``` and it should execute it in your Windows.

### Notes

For it to work, you must have not just ```php``` installed, but python as well.