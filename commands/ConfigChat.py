#Modulos Necessários

#import discord
#from discord.ext import commands
#from discord import app_commands
#from discord.ui import View
#import asyncio


@bot.tree.command(description="Configura o chat com opções como trancar, destrancar, fechar, reabrir, duplicar ou deletar o canal.")
@app_commands.describe(cargo="O cargo para configurar (Padrão = Everyone)")
async def configchat(interaction: discord.Interaction, cargo:discord.Role = None):
    autor = interaction.user
    canal = interaction.channel
    embedConfig = discord.Embed(title='Configuração de Chat')
    embedConfig.color = discord.Colour.orange()
    embedConfig.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2760/2760122.png')
    embedConfig.description = '''**Bem-Vindo(a) ao Painel de Configuração de Chat.**

**Selecione uma Opção:**\n\n

    **🔒 Trancar Canal**: Bloqueia o canal para impedir que os usuários enviem mensagens ou interajam até ser destrancado.\n\n
    **🔓 Destrancar Canal**: Remove as restrições e permite que os usuários interajam novamente no canal.\n\n
    **🚫 Fechar Canal**: Encerra temporariamente as atividades no canal, restringindo o envio de mensagens.\n\n
    **🔄 Reabrir Canal**: Reativa o canal fechado anteriormente, permitindo que as interações e conversas sejam retomadas.\n\n
    **➕ Duplicar Canal**: Cria uma cópia do canal atual com as mesmas configurações e permissões.\n\n
    **❌ Deletar Canal**: Remove o canal permanentemente do servidor, excluindo todas as mensagens e configurações.\n'''
    
    if cargo == None:
        RoleConfig = interaction.guild.default_role
    else:
        RoleConfig = cargo


    
    SelectPainel = discord.ui.Select(placeholder='Selecione um Opção')
    opçoes = [discord.SelectOption(label='Trancar Canal', value='Trancar', emoji='🔒'),
              discord.SelectOption(label='Destrancar Canal', value='Destrancar', emoji='🔓'),
              discord.SelectOption(label='Fechar Canal', value='Fechar', emoji='🚫'),
              discord.SelectOption(label='Reabrir Canal', value='Reabrir', emoji='🔄'),
              discord.SelectOption(label='Duplicar Canal', value='Duplicar', emoji='➕'),
              discord.SelectOption(label='Deletar Canal', value='Deletar', emoji='❌')]
    SelectPainel.options = opçoes
    
    async def OpçoesPainel(interaction: discord.Interaction):
        escolha = interaction.data['values'][0]
        embedInfo = discord.Embed(title='Padrão')
        embedInfo.set_footer(text='Sistema de Chats - 9ais')
        embedInfo.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2760/2760122.png')
        if escolha == 'Trancar':
            await canal.set_permissions(RoleConfig, read_messages=False)
            embedInfo.title = '🛠 - Acesso ao Chat Restrito'
            embedInfo.description = f'O acesso ao chat **{canal}** foi temporariamente restrito por {autor}.'
            embedInfo.color = discord.Colour.from_hsv(0, 1, 1)  # Vermelho
            
            await interaction.response.send_message(embed=embedInfo)

        elif escolha == 'Destrancar':
            await canal.set_permissions(RoleConfig, read_messages=True)
            embedInfo.title = '🛠 - Acesso ao Chat Liberado'
            embedInfo.description = f'O acesso ao chat **{canal}** foi restaurado por {autor}.'
            embedInfo.color = discord.Colour.from_hsv(0.33, 1, 1)  # Verde
            
            await interaction.response.send_message(embed=embedInfo)

        elif escolha == 'Fechar':
            await canal.set_permissions(RoleConfig, send_messages=False)
            embedInfo.title = '🛠 - Envio de Mensagens Bloqueado'
            embedInfo.description = f'O envio de mensagens no chat **{canal}** foi bloqueado por {autor}.'
            embedInfo.color = discord.Colour.from_hsv(0, 1, 1)  # Vermelho
            
            await interaction.response.send_message(embed=embedInfo)

        elif escolha == 'Reabrir':
            await canal.set_permissions(RoleConfig, send_messages=True)
            embedInfo.title = '🛠 - Envio de Mensagens Liberado'
            embedInfo.description = f'O envio de mensagens no chat **{canal}** foi liberado por {autor}.'
            embedInfo.color = discord.Colour.from_hsv(0.33, 1, 1)  # Verde
            
            await interaction.response.send_message(embed=embedInfo)

        elif escolha == 'Duplicar':
            novo_canal = await canal.clone(name=f"{canal.name}-cópia")
            await novo_canal.edit(position=canal.position + 1)
            embedInfo.title = '🛠 - Canal Duplicado'
            embedInfo.description = f'O Canal **{canal}** foi Duplicado como **{novo_canal}** por {autor}.'
            embedInfo.color = discord.Colour.from_hsv(0.58, 1, 1)  # Azul
            
            await interaction.response.send_message(embed=embedInfo)

        elif escolha == 'Deletar':
            embedInfo.title = '🛠 - Canal Deletado'
            embedInfo.description = f'O canal **{canal}** será permanentemente deletado em 5 segundos por {autor}.'
            embedInfo.color = discord.Colour.from_hsv(1, 1, 1)  # Cinza
            
            await interaction.response.send_message(embed=embedInfo)
            
            await asyncio.sleep(5)
            await canal.delete()
    
    view = View()
    view.add_item(SelectPainel)
    
    SelectPainel.callback = OpçoesPainel
    
    await interaction.response.send_message(embed=embedConfig, view=view, ephemeral=True)
