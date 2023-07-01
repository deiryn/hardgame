import discord
from discord.ext import commands, tasks
from datetime import datetime
from json import load
from random import randint
from os import listdir

config = load(open('config.json'))

from sys import platform
if platform == "win32":
    from ansicon import load
    load()

bot = commands.Bot(command_prefix="$", help_command=None, intents=discord.Intents.all())

#
class Images:
    def creep():
        '''
        returns creep.gif
        '''
        with open('images/creep.gif', 'rb') as file:
            return file.read()
    
    def day():
        '''
        returns day.gif
        '''
        with open('images/day.gif', 'rb') as file:
            return file.read()
    
    def daybez():
        '''
        returns daybez.gif
        '''
        with open('images/daybez.gif', 'rb') as file:
            return file.read()
    
    def dayBezdelie():
        '''
        returns dayBezdelie.gif
        '''
        with open('images/dayBezdelie.gif', 'rb') as file:
            return file.read()
    
    def dayGuitar():
        '''
        returns dayGuitar.gif
        '''
        with open('images/dayGuitar.gif', 'rb') as file:
            return file.read()
    
    def evening():
        '''
        returns evening.gif
        '''
        with open('images/evening.gif', 'rb') as file:
            return file.read()
    
    def eveningmusic():
        '''
        returns eveningmusic.gif
        '''
        with open('images/eveningmusic.gif', 'rb') as file:
            return file.read()
    
    def morning():
        '''
        returns morning.gif
        '''
        with open('images/morning.gif', 'rb') as file:
            return file.read()
        
    def morningbez():
        '''
        returns morningbez.gif
        '''
        with open('images/morningbez.gif', 'rb') as file:
            return file.read()
    
    def night():
        '''
        returns night.gif
        '''
        with open('images/night.gif', 'rb') as file:
            return file.read()
        
    def sleep():
        '''
        returns sleep.gif
        '''
        with open('images/sleep.gif', 'rb') as file:
            return file.read()
#

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")

    except Exception as e:
        print(e)
    changeBanner.start()
    print("\x1b[38;5;93mchangebanner\x1b[m || initialized")
    print('------')
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    activity = discord.Activity(name="ультракилл", type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)

dayStage = -1
'''
creep 0
day 1
daybez 2
dayBezdelie 3
dayGuitar 4
evening 5
eveningmusic 6
morning 7
morningbez 8
night 9
sleep 10
'''

@tasks.loop(minutes=1)
async def changeBanner():
    global dayStage
    guild = bot.get_guild(628323336790736896)
    if dayStage != 0 and datetime.now().hour >= 6 and datetime.now().hour < 7:
        dice = randint(1, 4)
        dayStage = 0
        if dice != 4:
            await guild.edit(reason="6:00 normal", banner=Images.morningbez())
            print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m | rolled {dice}")
        else:
            await guild.edit(reason="6:00 secret", banner=Images.creep())
            print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m | \x1b[48;5;196mrolled {dice}\x1b[m")
    
    elif dayStage != 1 and datetime.now().hour >= 7 and datetime.now().hour < 12:
        dayStage = 1
        await guild.edit(reason="7:00", banner=Images.morning())
        print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m")
   
    elif dayStage != 2 and datetime.now().hour >= 12 and datetime.now().hour < 15:
        dice = randint(1, 3)
        dayStage = 2
        match dice:
            case 1:
                await guild.edit(reason="12:00 1", banner=Images.day())
                print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m | rolled {dice}")
            case 2:
                await guild.edit(reason="12:00 2", banner=Images.dayGuitar())
                print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m | rolled {dice}")
            case 3:
                await guild.edit(reason="12:00 3", banner=Images.dayBezdelie())
                print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m | rolled {dice}")
    
    elif dayStage != 3 and datetime.now().hour >= 15 and datetime.now().hour < 16:
        dayStage = 3
        await guild.edit(reason="15:00", banner=Images.daybez())
        print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m")
    
    elif dayStage != 4 and datetime.now().hour >= 16 and datetime.now().hour < 18:
        dice = randint(1, 3)
        dayStage = 4
        match dice:
            case 1:
                await guild.edit(reason="16:00 1", banner=Images.day())
                print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m | rolled {dice}")
            case 2:
                await guild.edit(reason="16:00 2", banner=Images.dayGuitar())
                print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m | rolled {dice}")
            case 3:
                await guild.edit(reason="16:00 3", banner=Images.dayBezdelie())
                print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m | rolled {dice}")
   
    elif dayStage != 5 and datetime.now().hour >= 18 and datetime.now().hour < 22:
        dice = randint(1, 2)
        dayStage = 5
        match dice:
            case 1:
                await guild.edit(reason="18:00 1", banner=Images.evening())
                print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m | rolled {dice}")
            case 2:
                await guild.edit(reason="18:00 2", banner=Images.eveningmusic())
                print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m | rolled {dice}")
    
    elif dayStage != 6 and datetime.now().hour >= 22:
        dayStage = 6
        await guild.edit(reason="22:00", banner=Images.night())
        print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m")
    
    elif dayStage != 7 and datetime.now().hour >= 2 and datetime.now().hour < 6:
        dayStage = 7
        await guild.edit(reason="2:00", banner=Images.sleep())
        print(f"\x1b[38;5;93mchangebanner\x1b[m || \x1b[38;5;81m{datetime.now().hour}:{datetime.now().minute}\x1b[m")


@bot.tree.command(name="forcebanner")
@discord.app_commands.choices(banner=[
    discord.app_commands.Choice(name="creep", value=0),
    discord.app_commands.Choice(name="day", value=1),
    discord.app_commands.Choice(name="daybez", value=2),
    discord.app_commands.Choice(name="dayBezdelie", value=3),
    discord.app_commands.Choice(name="dayGuitar", value=4),
    discord.app_commands.Choice(name="evening", value=5),
    discord.app_commands.Choice(name="eveningmusic", value=6),
    discord.app_commands.Choice(name="morning", value=7),
    discord.app_commands.Choice(name="morningbez", value=8),
    discord.app_commands.Choice(name="night", value=9),
    discord.app_commands.Choice(name="sleep", value=10)
])
async def forceChange(interaction: discord.Interaction, banner: discord.app_commands.Choice[int]):
    guild = bot.get_guild(628323336790736896)
    match banner.value:
        case 0:
            await guild.edit(reason=f"forceChange by {interaction.user.name} to {banner.name}", banner=Images.creep())
        case 1:
            await guild.edit(reason=f"forceChange by {interaction.user.name} to {banner.name}", banner=Images.day())
        case 2:
            await guild.edit(reason=f"forceChange by {interaction.user.name} to {banner.name}", banner=Images.daybez())
        case 3:
            await guild.edit(reason=f"forceChange by {interaction.user.name} to {banner.name}", banner=Images.dayBezdelie)
        case 4:
            await guild.edit(reason=f"forceChange by {interaction.user.name} to {banner.name}", banner=Images.dayGuitar())
        case 5:
            await guild.edit(reason=f"forceChange by {interaction.user.name} to {banner.name}", banner=Images.evening())
        case 6:
            await guild.edit(reason=f"forceChange by {interaction.user.name} to {banner.name}", banner=Images.eveningmusic())
        case 7:
            await guild.edit(reason=f"forceChange by {interaction.user.name} to {banner.name}", banner=Images.morning())
        case 8:
            await guild.edit(reason=f"forceChange by {interaction.user.name} to {banner.name}", banner=Images.morningbez())
        case 9:
            await guild.edit(reason=f"forceChange by {interaction.user.name} to {banner.name}", banner=Images.night())
        case 10:
            await guild.edit(reason=f"forceChange by {interaction.user.name} to {banner.name}", banner=Images.sleep())
    print(f"[\x1b[38;5;93mchangebanner\x1b[m] \x1b[48;5;9mforceChange to {banner.name} by {interaction.user.name}")
    await interaction.response.defer(ephemeral=True)
    
bot.run(config["TOKEN"])