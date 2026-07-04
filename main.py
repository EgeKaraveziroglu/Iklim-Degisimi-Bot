import os
import random
import discord
from discord.ext import commands
from bot_token import bot_token


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)






neler_yapabiliriz = [
    " Enerji tasarrufu yapmak.",
    " Toplu taşıma, bisiklet veya yürüyüşü tercih etmek.",
    " Geri dönüşüme katkıda bulunmak.",
    " Tek kullanımlık plastik tüketimini azaltmak.",
    " Ağaç dikmek ve doğal alanları korumak."
]

etkileri = [
    " Küresel sıcaklıkların artması.",
    " Buzulların erimesi ve deniz seviyelerinin yükselmesi.",
    " Kuraklık, sel ve orman yangınları gibi aşırı hava olaylarının artması.",
    " Tarım ve su kaynaklarının olumsuz etkilenmesi.",
    " Bitki ve hayvan türlerinin yaşam alanlarının zarar görmesi."
]


@bot.command()
async def foto(ctx):
    secilen_foto = random.choice(os.listdir('images'))
    with open(f'images/{secilen_foto}', 'rb') as f:
        await ctx.send(file=discord.File(f))


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def nedir(ctx):
    await ctx.send(f'"İklim değişikliği, Dünyanın uzun vadeli sıcaklık ve hava koşullarındaki değişimlerdir. Doğal süreçler bu değişimlere neden olabilse de günümüzde en büyük etken insan faaliyetleridir. Fosil yakıtların (kömür, petrol ve doğal gaz) yakılması sonucunda atmosfere salınan sera gazları, Dünyanın daha fazla ısınmasına yol açmaktadır."') 

@bot.command()
async def etki(ctx):
    await ctx.send(f'{random.choice(etkileri)}')


@bot.command()
async def ne_yapmalıyız(ctx):
    await ctx.send(f'{random.choice(neler_yapabiliriz)}')


bot.run(bot_token)
