# Stock-Discord-Bot
**Overview**
- This project is a Discord Bot game implemented in Python which returns live stock and equities prices to a discord channel.
----
**Features**:
- `!quote` returns a full quote containing price, percent change, difference, and time
- `!price` returns price and ticker name
- `!percent_change` returns percent change of ticker and name
- `!change` returns the amount the equity lost or gained during the trading day
- `!futures` returns a full quote of VIX, and major E-Mini futures in an embeded image
- Implemented scrapper using BeautifulSoup4 to return live stock and equity prices from Yahoo Finance
- Testing functionality of scrapper and discord bot with Unittests

----

## Screen Shots
## Required Downloads for this Bot
1. Discord Account and Bot Token. The link to create a Discord Bot can be found here: 
[https://discord.com/developers/docs/game-sdk/applications](https://discord.com/developers/docs/game-sdk/applications)

2. Enter the token for the discord bot in the `key.json` file and enter the user agent into the `agent.json` file.
The link to determine your user agent can be found here:
[https://www.whatismybrowser.com/detect/what-is-my-user-agent/](https://www.whatismybrowser.com/detect/what-is-my-user-agent/)
## File Details
- *bot.py* - Contains the Discord Bot and scrapper
- *scrapper.py* - Allows to test the Discord Bot to ensure it is online
- *test_bot.py* - Unittest for commands of discord bot
- *test_scrapper.py* - Unittest for testing functionality of scrapper from Yahoo Finance
- *agent.json* - Stores the user agent information for scrapping
- *key.json* - Stores the Discord Bot Token

## To Run the Bot
1.  Download all the files from the repository.
2.  Run the *bot.py* file using `python bot.py`.
3.  Ensure the discord bot is added to server.
4.  A message should appear noting the discord bot is online `Logged on...`.


