import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.presences = True
intents.messages = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    update_status.start()

@tasks.loop(minutes=1)
async def update_status():
    game = discord.Game("Jersey")
    await bot.change_presence(activity=game)

bot.run('MTE4MzgyNTg1OTc0MDcwODkxNA.GG80lu.TQeLk4ig-oo43I-AFXS_GQ03t1PSGoMfWJtYqM')
