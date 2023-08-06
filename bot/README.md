# Work in progress
---
## Current Features
- Kei_bot sends an embed when joining a new server, indicates what prefix uses for the commands.
- Using a non blocking API call (doesn't stop the programm execution waiting for the response) with [aiohttp library](https://docs.aiohttp.org/en/stable/).
- Using "cogs", a way to group commands and other things. In this case, we can see the music_cog.
- Using the youtube_dl library to acces youtube videos through URL or keywords and play their audio.
---
### Commands
- `.!cat`: 😸Sends a random cat image using the catapi.
- `.!play [arg]`: 🎵Joins your voice channel and plays audio of given arg from youtube. You can also use the alias `.!p`.
