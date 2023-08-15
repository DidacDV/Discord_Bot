# Work in progress
---
## Current Features
- Kei_bot sends an embed when joining a new server, indicates what prefix uses for the commands.
- Using a non blocking API call (doesn't stop the programm execution waiting for the response) with [aiohttp library](https://docs.aiohttp.org/en/stable/).
- Using "cogs", a way to group commands and other things.
- Using the youtube_dl library to acces youtube videos through URL or keywords and play their audio.
---
## Commands
- `.!cat`: 😸Sends a random cat image using the catapi.
#### Music_cog
- `.!play [arg]`: 🎵Joins your voice channel and plays audio of given arg from youtube. You can also use the alias `.!p`.
- `.!pause`: ⏸️If bot is in a voice channel playing music, it will pause such music.
- `.!resume`: ▶️If a song has been paused, it resumes at the point where it was stopped.
- `.!skip`: ⏭️If a song is playing, it will be skipped an it will pass onto the next one.
- `list`: 📋Sends a message with all the current songs listed to play.
#### Gif_cog
- `.!gif [arg]`: 🖼️Sends a gif with the parameters given from user using the Tenor API. You can also use the alias `.!gf`
