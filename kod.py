import discord
from botmantik import gen_pass
import random 
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('merhaba bot'):
        await message.channel.send("selam")
        
    elif message.content.startswith('bay'):
        
    elif message.content.startswith('$sifre'):
        await message.channel.send(gen_pass(5))    
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("NO TOKEN")
