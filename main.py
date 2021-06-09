import discord
from discord.ext import commands
from config import settings
import datetime as dt

# bot = commands.Bot(command_prefix=settings['prefix'])
bot = discord.Client()


@bot.event
async def on_voice_state_update(member, before, after):
    time = str((dt.datetime.utcnow() + dt.timedelta(hours=5)).time())[:-7]
    user = f'**{str(member.display_name)}**'

    if before.channel is None:
        await bot.get_channel(792288140324634634).send(f'{user} `connect` to {after.channel.name} at {time}')

    elif not before.self_deaf and after.self_deaf:
        await bot.get_channel(792288140324634634).send(f'{user} `turn off` the sound and `mute` at {time}')

    elif before.self_deaf and not after.self_deaf:
        await bot.get_channel(792288140324634634).send(f'{user} `turn on` the sound and `unmute` at {time}')

    elif not before.self_mute and after.self_mute:
        await bot.get_channel(792288140324634634).send(f'{user} `mute` himself at {time}')

    elif before.self_mute and not after.self_mute:
        await bot.get_channel(792288140324634634).send(f'{user} `unmute` himself at {time}')

    elif not before.self_stream and after.self_stream:
        await bot.get_channel(792288140324634634).send(f'{user} `start stream` at {time}')

    elif before.self_stream and not after.self_stream:
        await bot.get_channel(792288140324634634).send(f'{user} `end stream` at {time}')

    elif not before.self_video and after.self_video:
        await bot.get_channel(792288140324634634).send(f'{user} `turn on camera` at {time}')

    elif before.self_video and not after.self_video:
        await bot.get_channel(792288140324634634).send(f'{user} `turn off camera` at {time}')

    elif before.channel is not None and after.channel is not None and after.channel != before.channel:
        mes = f'{user} `go` from {before.channel.name} to {after.channel.name} at {time}'
        await bot.get_channel(792288140324634634).send(mes)

    elif after.channel is None:
        await bot.get_channel(792288140324634634).send(f'{user} `leaves` us at {time}')

    else:
        await bot.get_channel(792288140324634634).send(f'{user} do something')


bot.run(settings['token'])
