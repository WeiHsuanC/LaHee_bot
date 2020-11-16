import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '#')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    joinChannel = bot.get_channel(777695761940086786)
    await joinChannel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    leaveChannel = bot.get_channel(777695761940086786)
    await leaveChannel.send(f'{member} leave!')

token = "Nzc3NTQwMTg0ODQwNjAxNjAw.X7E6ug.E-2In5NXOnqSW3I2w3XfRlPSXHU"
bot.run(token)