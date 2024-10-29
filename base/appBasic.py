import discord
from discord import app_commands
from discord.ext import commands

token = 'SeuTokenAqui'  # Coloque o Token do Bot
if token == 'SeuTokenAqui':
    # Aviso para adicionar o token caso não tenha sido definido
    print('\033[1;31mVocê precisa adicionar o Token do seu Bot.\033[m')

# Configuração de Intents, que são permissões específicas para o bot
intents = discord.Intents.default()  # Permissões padrão
intents.message_content = True  # Permissão para ler o conteúdo das mensagens
intents.members = True  # Permissão para ler e gerenciar os membros do servidor

# Instância do bot com prefixo '!' e os intents definidos acima
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # Evento ao iniciar o bot e confirmar que está online
    BotName = bot.user.name
    print(f'{BotName} está Online!')
    
    # Sincroniza os comandos de barra (Slash Commands) do bot
    sinc = await bot.tree.sync()
    print(f'Foram Sincronizados {len(sinc)} Comandos Slash')

@bot.command()
async def comando_base(cmd: commands.Context):
    # Comando de prefixo que responde ao usuário
    await cmd.reply(f'Olá {cmd.author.display_name}, Tudo bem? esse é um Comando Base de Prefixo.')
    # Seu Código adicional para esse comando aqui

@bot.tree.command()
async def comando_base(interaction: discord.Interaction):
    # Comando de barra (Slash) que responde ao usuário
    await interaction.response.send_message(f'Olá {interaction.user.display_name}, Tudo bem? Esse é um Comando Base Slash.')
    # Seu Código adicional para esse comando aqui

# Executa o bot se o token estiver configurado corretamente
if token != 'SeuTokenAqui':
    bot.run(token)
