import os
import discord
import requests
import asyncio
import logging
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ORDERS_CHANNEL_ID = int(os.getenv('ORDERS_CHANNEL_ID', 0))
SHEETDB_URL = os.getenv('SHEETDB_URL')

# Check for required env variables
if not TOKEN or not SHEETDB_URL or ORDERS_CHANNEL_ID == 0:
    raise ValueError("❌ One or more environment variables are missing. Please check .env file.")

# Constants
SELL_SHEET = "sell list"
BUY_SHEET = "buy list"

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Function to get selling price
def get_sell_price(item_name):
    try:
        response = requests.get(f"{SHEETDB_URL}/search?sheet={SELL_SHEET}&ITEM={item_name}")
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0].get('PRICE')
    except requests.RequestException as e:
        logger.error(f"Error fetching sell price: {e}")
    return None

# Function to get buying price
def get_buy_price(item_name):
    try:
        response = requests.get(f"{SHEETDB_URL}/search?sheet={BUY_SHEET}&ITEM={item_name}")
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0].get('PRICE')
    except requests.RequestException as e:
        logger.error(f"Error fetching buy price: {e}")
    return None

# Bot ready event
@bot.event
async def on_ready():
    logger.info(f'✅ Logged in as {bot.user.name} ({bot.user.id})')

# Price check command
@bot.command(name='pricecheck')
async def price_check(ctx, *, item_name: str = None):
    if not item_name:
        await ctx.send("❗ Please specify an item. Usage: `!pricecheck <item name>`")
        return
    price = get_sell_price(item_name)
    if price:
        await ctx.send(f"💰 The **selling price** for **{item_name}** is `{price}` aUEC.")
    else:
        await ctx.send(f"❌ Item **{item_name}** not found in the sell list.")

# Sell check command
@bot.command(name='sellcheck')
async def sell_check(ctx, *, item_name: str = None):
    if not item_name:
        await ctx.send("❗ Please specify an item. Usage: `!sellcheck <item name>`")
        return
    price = get_buy_price(item_name)
    if price:
        await ctx.send(f"📥 The **buying price** for **{item_name}** is `{price}` aUEC.")
    else:
        await ctx.send(f"❌ Item **{item_name}** not found in the buy list.")

# Place order command
@bot.command(name='placeorder')
async def place_order(ctx):
    try:
        await ctx.author.send(
            "**📝 Star Citizen Order Form**\n\n"
            "Please provide the following:\n"
            "1. Item(s) requested\n"
            "2. Quantity\n"
            "3. Special requests\n"
            "4. Deadline (if any)\n\n"
            "✏️ Reply here with your order details."
        )
        await ctx.send(f"{ctx.author.mention}, check your DMs for the order form!")

        def check(m):
            return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)

        try:
            msg = await bot.wait_for('message', check=check, timeout=600)

            embed = discord.Embed(
                title="📦 New Order Received",
                color=0x00ff00
            )
            embed.add_field(name="Customer", value=ctx.author.mention, inline=False)
            embed.add_field(name="Order Details", value=msg.content, inline=False)
            embed.set_footer(text=f"Order ID: {msg.id}")

            channel = bot.get_channel(ORDERS_CHANNEL_ID)
            if channel:
                await channel.send(embed=embed)
                await ctx.author.send("✅ Order submitted! Our team will contact you soon.")
            else:
                await ctx.author.send("❌ Error: Could not find the orders channel.")

        except asyncio.TimeoutError:
            await ctx.author.send("⌛ Order timed out. Please run `!placeorder` again.")

    except discord.Forbidden:
        await ctx.send(f"{ctx.author.mention}, I couldn't DM you! Please enable DMs in your privacy settings.")

# Start bot
if __name__ == '__main__':
    bot.run(TOKEN)

