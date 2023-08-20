import aiohttp
import random
import os
from discord.ext import commands

class Gif_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.quantity = 0
    
    async def get_gif(self, search):
        async with aiohttp.ClientSession() as session:  #creates session
            key = os.getenv("API_KEY")
            async with session.get("https://tenor.googleapis.com/v2/search?q={}&key={}&limit=120".format(search, key)) as resp:   #gets response from tenor
                print(resp.status)
                if resp.status == 200:     #checks if response is correct
                    resp = await resp.json()
                    choice = random.choice(resp['results'])
                    resp = choice['media_formats']['gif']['url']
                    return resp
                else:
                    return resp.status
    
    @commands.command(name="gif", aliases=["gf"])
    async def gif(self, ctx, *args):
        if not args:
            args = "random"
        await ctx.send(await self.get_gif(args))


async def setup(bot):
    await bot.add_cog(Gif_cog(bot))
