#instruções
#Antes de tudo, instalar a Biblioteca "pip install PyNaCl" no console

#Modulos

#import discord
#from discord.ext import commands

EntrarCall = False #Mude para "True" quando Adicionar o ID do Canal
IdCanalDeVoz = None  # Mude para o ID do Canal de Voz que o Bot irá Conectar

async def on_ready():
  if EntrarCall:
          canal = bot.get_channel(IdCanalDeVoz)  # Obtém o canal de voz pelo ID  
          if canal is not None and isinstance(canal, discord.VoiceChannel):  # Verifica se é um canal de voz
              await canal.connect()  # Conecta ao canal de voz, Lembre-se de Instalar "pip install PyNaCl"
              print(f'Bot conectado ao canal de voz: {canal.name}')
          else:
              print('Você não definiu um Canal de Voz válido.')
