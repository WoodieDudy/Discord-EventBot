# Discord EventBot

# About
> EventBot is a simple Discord bot that logs some user activity in channel
> 
### Running with docker
Set token and timezone variables in command below
```sh
docker run -d --restart unless-stopped --name event_bot -e TOKEN='abcde' -e TIME_ZONE=5 ghcr.io/woodiedudy/discord-eventbot:main
```
