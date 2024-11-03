#Modulos Necessarios

#import discord
#from discord.ext import commands
#import asyncio

@bot.event
async def on_ready():
  status = ['Use /comandos para Conhece-los', 'Precisa de Ajuda ? use /Help'] #Lista de Presenças para o Bot, Você pode colocar quantos Status preferir
  while True:
          for stats in status: #A Cada Stats em Status, setar a presença
              await bot.change_presence(status=discord.Status.online, activity=discord.Game(stats)) #Troca o Status do bot
              await asyncio.sleep(60) #A Cada 60 Segundos / 1 Minuto
