from urllib import request
import discord
import requests as requests
import time

client = discord.Client()
response = requests.get(f"https://api.opensea.io/collection/rubber-duck-bath-party")
@client.event
async def on_message(message):
  if message.content.find(".help") != -1:
    await message.channel.send("1. Command Prefix: . ")
    await message.channel.send("-----------------------")
    await message.channel.send("2. How to use it: \n.(command from those listed below)")
    await message.channel.send("-----------------------")
    await message.channel.send("3. List of supported commands: \n"
                              "\n3.1 - Daily:  .(floor price);  .(daily volume);  .(daily sales);  .(daily average price)\n"
                              "\n3.2 - Seven Day:  .(seven day volume);  .(seven day sales);  .(seven day average price)\n"
                              "\n3.3 - Thirty Day:  .(thirty day volume);  .(thirty day sales);  .(thirty day average price)\n"
                              "\n3.4 - Total Stats: .(total volume);  .(owners);  .(average price);  .(market cap)")

  if message.content.find(".floor price") != -1:
    await message.channel.send("Floor price: " + response.json().get("collection").get("stats").get("floor_price") + ("eth"))
    #await message.channel.send(response.json().get("collection").get("stats").get("floor_price"), ('eth'))
  if message.content.find(".daily volume") != -1:
    await message.channel.send("Daily volume (currency = ethereum): ")
    await message.channel.send(response.json().get("collection").get("stats").get("one_day_volume"))
  if message.content.find(".daily sales") != -1:
    await message.channel.send("Daily sales: ")
    await message.channel.send(response.json().get("collection").get("stats").get("one_day_sales"))
  if message.content.find(".daily average price") != -1:
    await message.channel.send("Daily average price (currency = ethereum): ")
    await message.channel.send(response.json().get("collection").get("stats").get("one_day_average_price"))
  if message.content.find(".seven day volume") != -1:
    await message.channel.send("Seven day volume (currency = ethereum): ")
    await message.channel.send(response.json().get("collection").get("stats").get("seven_day_volume"))
  if message.content.find(".seven day sales") != -1:
    await message.channel.send("Seven day sales: ")
    await message.channel.send(response.json().get("collection").get("stats").get("seven_day_sales"))
  if message.content.find(".seven day average price") != -1:
    await message.channel.send("Seven day average price (currency = ethereum): ")
    await message.channel.send(response.json().get("collection").get("stats").get("seven_day_average_price"))
  if message.content.find(".thirty day volume") != -1:
    await message.channel.send("Thirty day volume (currency = ethereum): ")
    await message.channel.send(response.json().get("collection").get("stats").get("thirty_day_volume"))
  if message.content.find(".thirty day sales") != -1:
    await message.channel.send("Thirty day sales: ")
    await message.channel.send(response.json().get("collection").get("stats").get("thirty_day_sales"))
  if message.content.find(".thirty day average price") != -1:
    await message.channel.send("Thirty day average price (currency = ethereum): ")
    await message.channel.send(response.json().get("collection").get("stats").get("thirty_day_average_price"))
  if message.content.find(".total volume") != -1:
    await message.channel.send("Total volume (currency = ethereum): ")
    await message.channel.send(response.json().get("collection").get("stats").get("total_volume"))
  if message.content.find(".total sales") != -1:
    await message.channel.send("Total sales: ")
    await message.channel.send(response.json().get("collection").get("stats").get("total_sales"))
  if message.content.find(".total supply") != -1:
    await message.channel.send("Total supply: ")
    await message.channel.send(response.json().get("collection").get("stats").get("total_supply"))
    await message.channel.send("items")
  if message.content.find(".owners") != -1:
    await message.channel.send("Total owners: ")
    await message.channel.send(response.json().get("collection").get("stats").get("num_owners"))
  if message.content.find(".average price") != -1:
    await message.channel.send("ALl time average price (currency = ethereum): ")
    await message.channel.send(response.json().get("collection").get("stats").get("average_price"))
  if message.content.find(".market cap") != -1:
    await message.channel.send("Total market cap (currency = ethereum): ")
    await message.channel.send(response.json().get("collection").get("stats").get("market_cap"))

@client.event
async def on_ready():
 #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                      # name="response.json().get(collection).get(stats).get(floor_price)"))

 def get_gas_from_ethgasstation(key: str, verbose: bool = False):
   r = requests.get('https://ethgasstation.info/api/ethgasAPI.json?')
   if r.status_code == 200:
     if verbose:
       print('200 OK')
     data = r.json()
     return int(data['fastest'] / 10), int(data['fast'] / 10), int(data['average'] / 10), int(
       data['safeLow'] / 10), int(data['fastestWait'] * 60), int(data['fastWait'] * 60), int(
       data['avgWait'] * 60), int(data['safeLowWait'] * 60)
   else:
     if verbose:
       print(r.status_code)
     time.sleep(10)
async def send_update(fastest, average, slow, **kw):
  status = f'⚡{fastest} |🐢{slow} | !help'
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,
                                                              name=status))

 #print('Bot is ready')


client.run('OTU2OTg2MDg5MDg2Nzk5ODgy.Yj4Mvw.1A_Hu3US7NDB9QpiZ7VLZoRSaTU')
