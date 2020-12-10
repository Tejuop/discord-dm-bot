import discord
import asyncio
from discord.ext import commands

token = '<your token!>'
bot = commands.Bot(command_prefix='T!') # Setting bot prefix to 'kk!'
# Send one dm!
# Usage: 'kk!dm 0000000000000000 My Message To You!!'
@bot.command()
async def dm(ctx, userid: int,*, dm: str):
    boi = bot.get_user(userid)
    await boi.send(dm)
    await ctx.send('DM send!')

# Send endless dm's! 
# Usage: 'kk!spam 00000000000000000 My Reapeated Message To You!!'
@bot.command()
async def spam(ctx, userid: int,*, dm: str):
    while True:
        boi = bot.get_user(userid)
        await boi.send(dm)
        await ctx.send('DM send!')

# Help!!!!
# Usage: 'T!nani'
@bot.command()
async def nani(ctx):
    embed = discord.Embed(
        title="HELP! U.u",
        color=discord.Colour(0x3b12ef),
        description="Commands:",
    )
    embed.add_field(
        name="kk!dm",
        value='Send a DM! (T!dm userid msg)'
    )
    embed.add_field(
        name="kk!spam",
        value="Spam in DM's! (T!spam userid msg)"
    )
    embed.add_field(
        name="kk!nani",
        value="Help!"
    )
    await ctx.send(
        embed=embed
    )

@bot.event
async def on_ready():
    name, id = bot.user.name, bot.user.id
    print('------\nLogged in with:\nUSER:%s\nID:%s\n------' % (name, id))

bot.run(token)
