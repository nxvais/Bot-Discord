#Modulos Necessarios

#import discord
#from discord import app_commands
#from discord.ui import Button, View




@bot.tree.command(description='Verifique as Informaçoes sobre esse Servidor')
async def serverinfo(interaction: discord.Interaction):
    embed_serverinfo = discord.Embed(title=f'Serverinfo - {interaction.guild.name}', color=discord.Color.blurple())
    
    if interaction.guild.icon:
        embed_serverinfo.set_thumbnail(url=interaction.guild.icon.url)
        BotaoIcon = Button(label='Imagem do Servidor', url=interaction.guild.icon.url, style=discord.ButtonStyle.url)
    
        view = View()
        view.add_item(BotaoIcon)
    else:
        embed_serverinfo.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/8890/8890972.png')
        BotaoIcon = Button(label='Imagem do Servidor', url='https://www.novais.com', style=discord.ButtonStyle.url, disabled=True)
    
        view = View()
        view.add_item(BotaoIcon)
    embed_serverinfo.add_field(name='Nome do Servidor', value=interaction.guild.name)
    embed_serverinfo.add_field(name='ID', value=interaction.guild.id)
    
    data_criacao = interaction.guild.created_at.strftime("%d/%m/%Y às %H:%M:%S")
    embed_serverinfo.add_field(name='Data de Criação', value=data_criacao, inline=False)
    
    embed_serverinfo.add_field(name='Criador(a)', value=f'O Servidor foi Criado por {interaction.guild.owner.mention}', inline=False)
    embed_serverinfo.add_field(name='Membros', value=f'O Servidor possui atualmente **{interaction.guild.member_count}** Membros', inline=False)
    embed_serverinfo.add_field(name='Cargos', value=f'O Servidor possui atualmente **{len(interaction.guild.roles)-1}** Cargos', inline=False)
    
    if interaction.guild.premium_subscription_count != 0:
        embed_serverinfo.add_field(name='Quantidade de Boosts', value=interaction.guild.premium_subscription_count)
