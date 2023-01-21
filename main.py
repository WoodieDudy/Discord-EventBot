import datetime as dt
import os

import discord
from discord.ext import commands


TOKEN = os.getenv("TOKEN")
TIME_ZONE = int(os.getenv("TIME_ZONE"))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

channels_to_log = {}


@bot.command()
async def loghere(ctx):
    if ctx.guild is None:
        return
    channels_to_log[ctx.guild.id] = ctx.channel.id
    await ctx.send('Okay. I will log to this channel.')


@bot.event
async def on_voice_state_update(member, before, after):
    time = (dt.datetime.utcnow() + dt.timedelta(hours=TIME_ZONE)).time().strftime("%H:%M")
    user = f'**{str(member.display_name)}**'
    guild_id = member.guild.id
    if guild_id not in channels_to_log:
        return
    channel = bot.get_channel(channels_to_log[guild_id])

    message = None
    if before.channel is None:
        message = f'{user} `connect` to {after.channel.name} at {time}'

    elif not before.self_stream and after.self_stream:
        message = f'{user} `start stream` at {time}'

    elif before.self_stream and not after.self_stream:
        message = f'{user} `end stream` at {time}'

    elif not before.self_video and after.self_video:
        message = f'{user} `turn on camera` at {time}'

    elif before.self_video and not after.self_video:
        message = f'{user} `turn off camera` at {time}'

    elif before.channel is not None and after.channel is not None and after.channel != before.channel:
        message = f'{user} `go` from {before.channel.name} to {after.channel.name} at {time}'

    elif after.channel is None:
        message = f'{user} `leaves` us at {time}'

    if message:
        await channel.send(message)


bot.run(TOKEN)
