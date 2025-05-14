# 🚀 Star Citizen Discord Bot

A lightweight Discord bot for tracking buy/sell prices and managing player-submitted orders in **Star Citizen**. Uses [SheetDB](https://sheetdb.io) to integrate Google Sheets as a simple backend.

## ✨ Features

- `!pricecheck <item>` – Get **sell price** of an item  
- `!sellcheck <item>` – Get **buy price** of an item  
- `!placeorder` – DM-based form submission with channel logging  

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/derwin130/star-citizen-discord-bot.git
cd star-citizen-discord-bot

# Install dependencies
pip install -r requirements.txt

# Create a .env file with your bot token
echo "DISCORD_TOKEN=your_discord_bot_token_here" > .env

# Edit the bot.py file and replace:
# - SHEETDB_URL with your SheetDB API URL
# - ORDERS_CHANNEL_ID with your Discord channel ID

# Run the bot
python bot.py
