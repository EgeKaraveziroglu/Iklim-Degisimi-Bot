import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def bilgi(ctx):
    await ctx.send(f'Geri dönüşüm yap, çöpü yere atma, suyu boşa harcama, elektriği tasarruflu kullan, ağaç dik, toplu taşıma kullan, plastik kullanımını azalt, doğayı kirletme, hayvanları koru, enerji tasarruflu ürünler kullan, atıkları ayrıştır, kimyasal madde kullanma, gürültü ve hava kirliliğini azalt, denizleri ve ormanları temiz tut, çevre temizliği etkinliklerine katıl, çevre bilinci yay."') 

bot.run("")
