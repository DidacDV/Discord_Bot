import discord 
import os
from dotenv import load_dotenv
from discord.ext import commands
#bot 29/07/2023

bot_test = commands.Bot(command_prefix= '.', intents=discord.Intents.all())  #What prefix will the bot use to execute its commands + getting all intents
load_dotenv()
token = os.getenv("TOKEN")  #GETS TOKEN FROM ENV FILE


@bot_test.event
async def on_ready():       #Coroutine
    print("Ready to start!")                    #OUTPUT FOR COMMAND LINE
    print(f"Bot discord tag = {bot_test.user}")

@bot_test.event
async def on_guild_join(guild):         #WHEN BOT JOINS SERVER(GUILD)
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me):                              #LOOKS FOR CHANNEL TO PRINT WHEN JOINING
            desc = "This is a test bot by [DidacDV](https://github.com/DidacDV)."
            embed = discord.Embed(title= "kei_bot",color= discord.Color.blurple())
            embed.description = desc
            embed.set_author(name= "kei_bot", url = "https://github.com/DidacDV", icon_url="https://i.imgur.com/yucaCxs.jpeg")
            await channel.send(embed = embed)
            break

@bot_test.command()
async def test(ctx):        #ctx = Context object
    await ctx.send("test")
 
bot_test.run(token) 
