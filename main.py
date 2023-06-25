import discord
from discord.ext import commands, tasks
from datetime import datetime
from json import load

config = load(open('config.json'))

from sys import platform
if platform == "win32":
    from ansicon import load
    load()

bot = commands.Bot(command_prefix="$", help_command=None, intents=discord.Intents.all())

nightIcon = ""
dayIcon = ""
with open('1.gif', 'rb') as file:
    nightIcon = file.read()

with open('2.gif', 'rb') as file:
    dayIcon = file.read()

#with open('НАЗВАНИЕ ФАЙЛА', 'rb') as file:
#    ПЕРЕМЕННАЯ = file.read()

#with open('НАЗВАНИЕ ФАЙЛА', 'rb') as file:
#    ПЕРЕМЕННАЯ = file.read()

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")

    except Exception as e:
        print(e)
    changeBanner.start()
    print('------')
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    activity = discord.Activity(name="ультракилл", type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)

@tasks.loop(minutes=1)
async def changeBanner():
    print("changeBanner")
    guild = bot.get_guild(628323336790736896)
    if datetime.now().hour >= 6 and datetime.now().hour < 12:
        await guild.edit(reason="6:00", banner=dayIcon)
    elif datetime.now().hour >= 12 and datetime.now().hour < 18:
        await guild.edit(reason="12:00", banner=dayIcon)
    elif datetime.now().hour >= 18 and datetime.now().hour < 0:
        await guild.edit(reason="18:00", banner=nightIcon)
    elif datetime.now().hour >= 0 and datetime.now().hour < 6:
        await guild.edit(reason="00:00", banner=nightIcon)

@bot.tree.command(name="forcebanner")
@discord.app_commands.choices(banner=[
    discord.app_commands.Choice(name="1", value=1),
    discord.app_commands.Choice(name="2", value=2),
    discord.app_commands.Choice(name="3", value=3),
    discord.app_commands.Choice(name="4", value=4)
])
async def forceChange(interaction: discord.Interaction, banner: discord.app_commands.Choice[int]):
    guild = bot.get_guild(628323336790736896)
    if banner.value == 1:
        await guild.edit(reason=f"меня заставили ({interaction.user.name})", banner=nightIcon)
        await interaction.response.send_message("это ты конечно классно поменял баннер этого сервера на ноч, да............", ephemeral=True)
    elif banner.value == 2:
        await guild.edit(reason=f"меня заставили ({interaction.user.name})", banner=dayIcon)
        await interaction.response.send_message("это ты конечно классно поменял баннер этого сервера на ден, да............", ephemeral=True)
    elif banner.value == 3:
        #await guild.edit(reason=f"меня заставили ({interaction.user.name})", banner=ПЕРЕМЕННАЯ ФАЙЛА)
        await interaction.response.send_message("этого файла еще нет, поэтому мы тебя жестко затроллили <:HG_biper_clown:885954760124039188>", ephemeral=True)
    elif banner.value == 4:
        #await guild.edit(reason=f"меня заставили ({interaction.user.name})", banner=ПЕРЕМЕННАЯ ФАЙЛА)
        await interaction.response.send_message("этого файла еще нет, поэтому мы тебя жестко затроллили <:HG_biper_clown:885954760124039188>", ephemeral=True)
    

bot.run(config["TOKEN"])