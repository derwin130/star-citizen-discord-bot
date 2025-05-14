# 🚀 Star Citizen Discord Bot

A lightweight Discord bot for tracking buy/sell prices and managing player-submitted orders in **Star Citizen**. Uses [SheetDB](https://sheetdb.io) to integrate Google Sheets as a simple database backend.

---

## ✨ Features

- `!pricecheck <item>` – Get **sell price** of an item
- `!sellcheck <item>` – Get **buy price** of an item
- `!placeorder` – Collect order details via DM and log them in a dedicated channel

---

## 📦 Tech Stack

- [Python 3.x](https://www.python.org/)
- [discord.py](https://github.com/Rapptz/discord.py)
- [SheetDB API](https://sheetdb.io)
- `.env` for secure config handling

---

## ⚙️ Setup

1. **Clone the repo**

```bash
git clone https://github.com/derwin130/star-citizen-discord-bot.git
cd star-citizen-discord-bot


2. **Install dependencies**

bash
Copy
Edit
pip install -r requirements.txt


3. **Set up environment variables**

Create a .env file in the root directory:

env
Copy
Edit
DISCORD_TOKEN=your_discord_bot_token


4 **Edit constants in bot.py**

SHEETDB_URL: Your SheetDB API endpoint

ORDERS_CHANNEL_ID: The Discord channel ID where orders should be posted


▶️ Running the Bot
bash
Copy
Edit
python bot.py

🧪 Example Usage
!pricecheck Laranite
!sellcheck Titanium
!placeorder

🙌 Contributing
Contributions welcome! Feel free to open issues or submit pull requests.

📄 License
This project is open source and available under the MIT License.

🧠 Credits
Made with ❤️ by derwin130 for the Star Citizen community.

yaml
Copy
Edit

---

✅ Just paste the above into a file named `README.md` in your repo and commit it:

```bash
git add README.md
git commit -m "Add README"
git push
