import discord
import requests as requests
from discord.ext import tasks
from typing import Final, Optional, Coroutine, Dict
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix = ".")
response = requests.get(
  "https://api.opensea.io/collection/rubber-duck-bath-party"
)
client.remove_command("help")

STATS = response.json().get("collection").get("stats")

@client.command()
async def help(ctx: commands.Context):
    await ctx.send("""1. Command Prefix: .
-----------------------
2. How to use it: \n.(command from those listed below)
-----------------------
3. List of supported commands: 
3.1 - Daily:  .(daily volume);  .(daily sales);  .(daily average price)"
3.2 - Seven Day:  .(seven day volume);  .(seven day sales);  .(seven day average price)"
3.3 - Thirty Day:  .(thirty day volume);  .(thirty day sales);  .(thirty day average price)"
3.4 - Overall Stats: .(total supply) .(total volume);  .(total owners);  .(average price);  .(market cap)""")

async def _handle(
    ctx: commands.Context,
    key: str,
    force_fmt: Optional[str] = None,
    price: bool = True
):
    fmt: str = force_fmt or key \
        .replace('_', ' ') \
        .capitalize()

    await ctx.send(f"{fmt}{'' if price else ''}: {STATS.get(key)}")

#@client.command()
#async def floor(ctx: commands.Context, arg: str):
    #if arg == 'price':
        #await _handle(ctx, "floor_price")

async def _coros(coros: Dict[str, Coroutine], key: str):
    if coro := coros.get(key):
        await coro

@client.command()
async def daily(ctx: commands.Context, *, arg: str):
    await _coros({
        'volume': _handle(ctx, "one_day_volume", "Daily volume"),
        'sales': _handle(ctx, "one_day_sales", "Daily sales", False),
        'average price': _handle(ctx, "one_day_average_price", "Daily average price")
    }, arg)

@client.command()
async def seven(ctx: commands.Context, *, arg: str):
    await _coros({
        'day volume': _handle(ctx, "seven_day_volume"),
        'day sales': _handle(ctx, "seven_day_sales", price=False),
        'average price': _handle(ctx, "seven_day_average_price")
    }, arg)

@client.command()
async def thirty(ctx: commands.Context, *, arg: str):
    await _coros({
        'day volume': _handle(ctx, "thirty_day_volume"),
        'day sales': _handle(ctx, "thirty_day_sales", price=False),
        'day average price': _handle(ctx, "thirty_day_average_price")
    }, arg)

@client.command()
async def total(ctx: commands.Context, arg: str):
    await _coros({
        'volume': _handle(ctx, "total_volume"),
        'sales': _handle(ctx, "total_sales", price=False),
        'supply': _handle(ctx, "total_supply", price=False),
        'owners': _handle(ctx, "num_owners", price=False)
    }, arg)

@client.command()
async def average(ctx: commands.Context, arg: str):
    if arg == "price":
        await _handle(ctx, "average_price", "All time average price")

@client.command()
async def market(ctx: commands.Context, arg: str):
    if arg == "cap":
        await _handle(ctx, "market_cap")

@tasks.loop(seconds= 60)
async def loop():
    amount: float = requests.get("https://api.opensea.io/api/v1/collection/rubber-duck-bath-party/stats").json()['stats']['floor_price']
    activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f"Floor Price: {amount} Eth"
    )

    await client.change_presence(activity = activity)
    await asyncio.sleep(60)

@client.event
async def on_ready():
    loop.start()
    print('The Bot is Ready!')

client.run('{replace with key}')
