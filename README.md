# Discord_Bot
Using python and the discord library to create a discord bot.

![kei bot](https://github.com/DidacDV/Discord_Bot/blob/main/images/bot_logo2.jpg) 

`Kei bot logo.`
## Process
Currently working on this project, mainly using the documentation for the [discord python library](https://discordpy.readthedocs.io/en/latest/api.html#discord.Embed.author). While learning this library, i'm also getting into [coroutines and tasks with python](https://docs.python.org/3/library/asyncio-task.html) (with that not being the main goal). 

---
## Current Features
- Kei_bot sends an embed when joining a new server, indicates what prefix uses for the commands.
- Using a non blocking API call (doesn't stop the programm execution waiting for the response) with [aiohttp library](https://docs.aiohttp.org/en/stable/).
- Using "cogs", a way to group commands and other things.
- Using the youtube_dl library to acces youtube videos through URL or keywords and play their audio.
- Getting latitude/altitude with geopy and using it to get the temperature on a desired city with an API.
---
## Commands
- `.!weather [city] [days]`: Sends a table containing the temperature expected for each hour at [city] in a range of [days] from the moment the command is executed. Days argument is optional and set to 1 by default.
- `.!cat`: 😸Sends a random cat image using the catapi.
#### Music_cog
- `.!play [arg]`: 🎵Joins your voice channel and plays audio of given arg from youtube. You can also use the alias `.!p`.
- `.!pause`: ⏸️If bot is in a voice channel playing music, it will pause such music.
- `.!resume`: ▶️If a song has been paused, it resumes at the point where it was stopped.
- `.!skip`: ⏭️If a song is playing, it will be skipped an it will pass onto the next one.
- `.!list`: 📋Sends a message with all the current songs listed to play.
#### Gif_cog
- `.!gif [arg]`: 🖼️Sends a gif with the parameters given from user using the Tenor API. You can also use the alias `.!gf`
