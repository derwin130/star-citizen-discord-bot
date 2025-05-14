# 🚀 Star Citizen Discord Bot

A lightweight Discord bot for tracking buy/sell prices and managing player-submitted orders in **Star Citizen**. Uses [SheetDB](https://sheetdb.io) to integrate Google Sheets as a simple backend.

## 📦 Tech Stack

- Python 3.x  
- discord.py  
- SheetDB API  
- `.env` for secure config handling  

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/derwin130/star-citizen-discord-bot.git
cd star-citizen-discord-bot
````

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set up environment variables

Create a `.env` file in the project root:

```env
DISCORD_TOKEN=your_discord_bot_token
```

---

### 4. Edit constants in `bot.py`

Replace the following with your actual values:

* `SHEETDB_URL`: Your SheetDB API endpoint
* `ORDERS_CHANNEL_ID`: The ID of your Discord channel for receiving orders

---

### 5. Run the bot

```bash
python bot.py
```

---

## 🧪 Example Commands

```plaintext
!pricecheck Laranite
!sellcheck Titanium
!placeorder
```

---

## 🤝 Contributing

Pull requests and ideas are welcome!

---

## 📄 License

This project is licensed under the MIT License.

```

---

✅ **To apply it:**
1. Open your repo on GitHub.
2. Click `Add file` → `Create new file`.
3. Name it `README.md`.
4. Paste the content above.
5. Commit to `main`.

Let me know if you also want me to generate a matching `requirements.txt`!
```
