import discord 
import os
import aiohttp
from geopy.geocoders import Nominatim
from music_cog import Music_cog
from gif_cog import Gif_cog
from dotenv import load_dotenv
from table2ascii import table2ascii as t2a, PresetStyle
from discord.ext import commands
#bot 29/07/2023

bot_test = commands.Bot(command_prefix= '.!', intents=discord.Intents.all())   #prefix for the bot use to execute its commands + getting all intents
load_dotenv()
token = os.getenv("TOKEN")  #GETS TOKEN FROM ENV FILE
key = os.getenv("API_KEY")  #GETS TENOR API KEY FROM ENV FILE


@bot_test.event
async def on_ready():
    await bot_test.load_extension('music_cog')
    await bot_test.load_extension('gif_cog')
    print("Ready to start!")                    
    print(f"Bot discord tag = {bot_test.user}")

@bot_test.event
async def on_guild_join(guild):         #EXECUTES WHEN JOINING SERVER(GUILD)
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me):                              #looks for channel to print
            desc = "This is a test bot by [DidacDV](https://github.com/DidacDV)\n\nMy **prefix** for commands is **.!**\n\nType **.!help** to see all commands"
            embed = discord.Embed(title= "Kei_bot",color= discord.Color.dark_gold())
            embed.description = desc
            embed.set_author(name= "Kei_bot", icon_url="https://i.imgur.com/yucaCxs.jpeg")
            await channel.send(embed = embed)
            break




@bot_test.command()
async def leave(ctx):
    status = ctx.voice_client                       #checks if user is in a voice channel
    if status != None:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("You have to be in a voice channel to run this command")



@bot_test.command()
async def cat(ctx):        #CAT COMMAND
    async with aiohttp.ClientSession() as session:  #creates session
        async with session.get("https://api.thecatapi.com/v1/images/search") as resp:   #gets response from catapi
            if resp.status == 200:     #checks if response is correct
                resp = await resp.json()
                resp = resp[0]['url']
                await ctx.send(resp)        #sends URL that appears as cat image
                await ctx.send('Meow! 😺😺😺')


@bot_test.command()
async def weather(ctx, city, *days):
        #Getting the coordinates of the city so that we can use the API
        # Initialize Nominatim API
        location = Nominatim(user_agent="disc_bot")
        location = location.geocode(city)
        if location:
            longitude = location.longitude
            latitude = location.latitude
            await ctx.send(longitude)
            await ctx.send(latitude)
            if not days:
                days[0] = 1
            async with aiohttp.ClientSession() as session:  
                async with session.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&forecast_days={days[0]}") as resp:   #gets response from catapi
                    if resp.status == 200:     
                        resp = await resp.json()
                        resp = resp["hourly"]
                        collecter = []
                        i = 0
                        for value in resp["time"]:
                            dt = [value,resp["temperature_2m"][i]]
                            collecter.append(dt)
                            i += 1
                        table = t2a(
                            header = ["Date/Time" ,"Temperature"],
                            body = collecter,
                            style= PresetStyle.thin_compact
                        )
                        await ctx.send(f"```\n{table}\n```")                
                    else:
                        await ctx.send(resp.status)
        else:
            await ctx.send("Location not found 😔")       
#have to implement weather code + response with emoji / gif

bot_test.run(token) 
