import discord

from discord.ext import commands

import random

 

intents = discord.Intents.default()

intents.message_content = True

 

bot = commands.Bot(command_prefix='b-', intents=intents)

 

@bot.event

async def on_ready():

    print(f'logado como {bot.user}')
    print(f'mande b-hello no chat para ver as imagens!')

 

@bot.command()

async def hello(ctx):

    await ctx.send('Hello! Here are some images for you! its a joke that only speedrunners can understand!:')

    with open('Dbot/images/bed.jpeg', 'rb') as images:
        picture = discord.File(images)
        await ctx.send(file=picture)

    with open('Dbot/images/plus.png', 'rb') as images:
        picture = discord.File(images)
        await ctx.send(file=picture)

    with open('Dbot/images/enderdragon.jpeg', 'rb') as images:
        picture = discord.File(images)
        await ctx.send(file=picture)

    with open('Dbot/images/equ.png', 'rb') as images:
        picture = discord.File(images)
        await ctx.send(file=picture)

    with open('Dbot/images/die.jpeg', 'rb') as images:
        picture = discord.File(images)
        await ctx.send(file=picture)

    await ctx.send('whats your reaction? type b-kkk to like ans nothing for dont like')


@bot.command()

async def kkk(ctx, count_kk = 5):

    await ctx.send("kk" * count_kk)



bot.run("MTQ0OTQwMDcxMDMxMDUzMTIyMA.GlvInZ.dHMr0FtNC3nD2GnT9ly815bC1bqyBjjfI7Z4VI")
