import discord 
from  youtube_dl import YoutubeDL
from discord.ext import commands

class Music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.playing = False
        self.paused = False
        self.songqueue = []
        self.ytdl_format_options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0', 
        }
        self.ffmpeg_options = {'before options': '-reconnect 1 -reconnected_streamed 1 -reconnect_delay_max 5','options': '-vn'}
    def yt_url(self, ms):                               #SEARCHES FIRST RESULT FROM URL AT YT
        with YoutubeDL(self.ytdl_format_options) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % ms, download = False)['entries'][0]
            except:
                return False
        return {'source': info['formats'][0]['url'], 'title': info['title']}
    
    def next(self):
        if len(self.songqueue) != 0:
            ur = self.songqueue[0][0]['source']         #getting the URL from the song to play
            self.songqueue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(ur, **self.ffmpeg_options), after =lambda e: self.next())
            self.playing = True
        else:
            self.playing = False
    
    async def initialize(self, ctx):
        if len(self.songqueue) != 0:
            ur = self.songqueue[0][0]['source']
            if self.vc == None:
                self.vc = await self.songqueue[0][1].connect()
                if self.vc == None:
                    await ctx.send("Not able to conenct to voice channel")
                    return 0
            else:
                await self.vc.move_to(self.songqueue[0][1])
            self.songqueue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(ur, **self.ffmpeg_options), after =lambda e: self.next())
            self.playing = True
        else:
            self.playing = False

    @commands.command(name="play", aliases=["p"])
    async def play(self, ctx, *args):
        search = " ".join(args)
        vch = ctx.author.voice.channel
        if vch is None:
            await ctx.send("You have to be in a voice channel to run this command")
        elif self.paused:
            self.vc.resume()
        else:
            song = self.yt_url(search)
            if song == False:
                await ctx.send("Song couldn't be found, try again with other keywords")
            else:
                await ctx.send("Song has been added to the queue")
                self.songqueue.append([song, vch])
                
                if self.playing == False:
                    await self.initialize(ctx)


    @commands.command(name="pause")
    async def pause(self, ctx, *args):
        if self.playing:
            self.playing = False
            self.paused = True
            self.vc.pause()
    @commands.command(name="resume")
    async def resume(self, ctx, *args):
        if self.paused:
            self.paused = False
            self.playing = True
            self.vc.resume()
    @commands.command(name = "skip")    #skips song
    async def skip(self, ctx, *args):
        if self.playing:
            if self.vc:
                self.vc.stop()
                await self.play(ctx)
        else:
            await ctx.send("No song playing :(")
    @commands.command(name="list")
    async def list(self, ctx, *args):
        exist = False
        songs = ""
        if len(self.songqueue) != 0:
            exist = True
            for song in self.songqueue:
                songs += song[0]['title']
                song += '\n'
        if exist:
            await ctx.send(songs)
        else:
            await ctx.send("No songs in queue :(")

async def setup(bot):
    await bot.add_cog(Music_cog(bot))