# TeleChuck_bot
A telegram bot that tells Chuck Norris Jokes.

## How to use TeleChuck_bot?
To use TeleChuck_bot you can simply DM it or add it to groups. You may find it [here](https://t.me/TeleChuck_bot).

## What can TeleChuck_bot do?
TeleChuck_bot can tell Chuck Norris jokes provided by the [list](https://parade.com/968666/parade/chuck-norris-jokes/).


To interact with TeleChuck_bot you can send it the following commands:

`gimme` (ignores lower/upper case) (short of give-me): TeleChuck_bot will randomly reply this message with one of it's jokes.

`gimme <x>` (ignores lower/upper case): TeleChuck_bot will reply this message with the corresponding joke. Note that `x` must be an integer between 1 and 101 (inclusive). 

`/help` or `/start`: TeleChuck_bot will provide information about it's capabilities and functionalities.

## Code:
To use the TeleChuck_bot code you first must install the [telebot](https://github.com/eternnoir/pyTelegramBotAPI) and the [bs4](https://pypi.org/project/beautifulsoup4/) libraries.

Now to run the code - simply run `python main.py`.

### About the project's structure:

I have created two files to perform the operation:

**main.py** that is responsible for the Telegram comunication.
It uses the telebot library and defines the behavior of the bot in the case of receiving certain messages (with those `message_handler`s).

<br/>

**jokepuller.py** that scrapes the actual jokes from the provided website.

It uses the b64 library and loads (one time) all the jokes into a local list and then returns the corresponding joke from it.

To scrape only the jokes it takes only the phrases between `<li> </li>` tags that are also contain either 'Chuck' or 'Norris'.

<br/><br/>
TeleChuck_bot is currently running from an AWS-ec2.
