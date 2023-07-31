import discord 
import os
import aiohttp
from dotenv import load_dotenv
from discord.ext import commands
#bot 29/07/2023

bot_test = commands.Bot(command_prefix= '.!', intents=discord.Intents.all())   #prefix for the bot use to execute its commands + getting all intents
load_dotenv()
token = os.getenv("TOKEN")  #GETS TOKEN FROM ENV FILE


@bot_test.event
async def on_ready():       
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
async def cat(ctx):        #CAT COMMAND
    async with aiohttp.ClientSession() as session:  #creates session
        async with session.get("https://api.thecatapi.com/v1/images/search") as resp:   #gets response from catapi
            if resp.status == 200:     #checks if response is correct
                resp = await resp.json()
                resp = resp[0]['url']
                await ctx.send(resp)        #sends URL that appears as cat image


bot_test.run(token) 
