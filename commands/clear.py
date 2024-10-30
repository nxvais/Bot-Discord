#Modulos Necessarios

#import discord
#from discord import app_commands
#from discord.ext import commands
#from asyncio import sleep


@bot.tree.command()
@app_commands.describe(quantidade='Número de mensagens a serem apagadas')
async def clear(interaction: discord.Interaction, quantidade: int):
    user = interaction.user
    
    # Verifica se o usuário tem permissão para gerenciar mensagens
    if not interaction.channel.permissions_for(user).manage_messages:
        embedPermError = discord.Embed(
            title='⚠️ Permissão Insuficiente',
            description=f'{user.mention}, você não tem permissão para apagar mensagens neste canal.',
            color=discord.Colour.dark_red()
        )
        await interaction.response.send_message(embed=embedPermError, ephemeral=True)
        return
    
    # Verifica se o bot tem permissão para apagar mensagens
    if not interaction.channel.permissions_for(interaction.guild.me).manage_messages:
        embedBotPermError = discord.Embed(
            title='⚠️ Erro de Permissão do Bot',
            description='Não tenho permissão para apagar mensagens neste canal. Por favor, ajuste as permissões.',
            color=discord.Colour.dark_red()
        )
        await interaction.response.send_message(embed=embedBotPermError, ephemeral=True)
        return
    
    # Verifica se o valor é válido
    if quantidade <= 0:
        embedClear = discord.Embed(
            title='⚠️ Valor Inválido',
            description='Digite um valor maior que 0 para apagar mensagens.',
            color=discord.Colour.dark_red()
        )
        await interaction.response.send_message(embed=embedClear, ephemeral=True)
        return
    
    # Confirmação inicial da limpeza
    embedClearStart = discord.Embed(
        title='🧹 Iniciando Limpeza...',
        description=f'Apagando até {quantidade} mensagens em {interaction.channel.mention}...',
        color=discord.Colour.green()
    )
    await interaction.response.send_message(embed=embedClearStart, ephemeral=True)
    
    await sleep(1)  # Pequeno atraso para dar feedback antes de iniciar
    
    # Executa a purga de mensagens
    mensagens_apagadas = await interaction.channel.purge(limit=quantidade)
    total_apagadas = len(mensagens_apagadas)
    
    # Confirmação final da limpeza
    embedClearEnd = discord.Embed(
        title='✅ Chat Limpo!',
        description=f'{total_apagadas} mensagens foram apagadas com sucesso por {user.mention}.',
        color=discord.Colour.blue()
    )
  
    await interaction.channel.send(embed=embedClearEnd, delete_after=5)
