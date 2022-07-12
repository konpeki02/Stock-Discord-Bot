import json


import discord
from discord.ext import commands
from src import scrapper

bot = commands.Bot(command_prefix='!')


def getKey(filename, target):
    with open(filename) as f:
        data = json.load(f)
        token = data[target]
        return token


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if message.content.startswith(message):
        await message.channel.send(message)


@bot.command(pass_context=True)
async def quote(ctx, arg):
    try:
        user_quote = '%s: %s' % (arg.upper(), scrapper.find_price(arg.upper()))
        await ctx.channel.send(user_quote)
    except (Exception,):
        await ctx.channel.send('Enter Valid Ticker, ref = https://finance.yahoo.com')
        pass




@bot.command(pass_context=True)
async def price(ctx, arg):
    try:
        user_quote = '%s: %s' % (arg.upper(), scrapper.find_price(arg.upper()))
        await ctx.channel.send(scrapper.get_price(user_quote))
    except:
        await ctx.channel.send('Enter Valid Ticker, ref = https://finance.yahoo.com')


@bot.command(pass_context=True)
async def percent_change(ctx, arg):
    try:
        user_quote = '%s: %s' % (arg.upper(), scrapper.find_price(arg.upper()))
        await ctx.channel.send(scrapper.get_percent_change(user_quote))
    except:
        await ctx.channel.send('Enter Valid Ticker, ref = https://finance.yahoo.com')


@bot.command(pass_context=True)
async def change(ctx, arg):
    try:
        user_quote = '%s: %s' % (arg.upper(), scrapper.find_price(arg.upper()))
        await ctx.channel.send(scrapper.get_change(user_quote))
    except:
        await ctx.channel.send('Enter Valid Ticker, ref = https://finance.yahoo.com')


@bot.command(pass_context=True)
async def futures(ctx):
    vix = 'VIX = ' + scrapper.get_just_quote(scrapper.find_price('^VIX'))
    es = '\ES = ' + scrapper.get_just_quote(scrapper.find_price('ES=F'))
    nq = '\\NQ = ' + scrapper.get_just_quote(scrapper.find_price('NQ=F'))
    rty = '\RTY = ' + scrapper.get_just_quote(scrapper.find_price('RTY=F'))
    ym = '\YM = ' + scrapper.get_just_quote(scrapper.find_price('YM=F'))
    futures_quote = '%s\n%s\n%s\n%s\n%s\n' % (vix, es, nq, rty, ym)
    embed = discord.Embed(title='', description=futures_quote, color=0x00ff00)
    await ctx.channel.send(embed=embed)

bot.run(getKey('key.json', 'key'))
