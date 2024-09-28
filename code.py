import discord, random, os, requests
from discord.ext import commands
description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

@bot.command()
async def help_nature(ctx):
    await ctx.send("Привет! Хочешь помочь сохранить природу? Вот базовые знания о материалах, которые ты используешь в быту!")
    await ctx.send("- Пластик - ты знаком с этим - бутылки, пакеты и т.д., но разлагаеться эта вещь 400-700 лет! Представь, что будет, если 1к людей выкинет пластик в природу!")
    await ctx.send("- Стекло - вторая вещь, которой пользуются многие, окна, например. Разлагается оно больше тысячи лет! Да, стекло вернётся обратно в песок, но всё же..")
    await ctx.send("- Алюминий - банки из под Колы состоят из него, а разлагается - 500 лет. Тоже неприятно ходить по банках спустя 200 лет, не так ли?")
    await ctx.send("- Жесть - нет, это не 18+ сцены с кровью и трупами, это жестянки - консервы и т.д., разложение - до 90 лет")

intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
bot.run("key")
