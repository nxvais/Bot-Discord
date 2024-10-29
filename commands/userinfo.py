#Modulos Necessarios

#import discord
#from discord import app_commands
#from datetime import timezone




@bot.tree.command(description='Verifique as Informaçoes sobre um Usuario')
@app_commands.describe(usuario='Usuario que irei ver as Informações')
async def userinfo(interaction: discord.Integration, usuario:discord.Member = None):
    if usuario == None:
        usuario = interaction.user
    user_id = usuario.id
    user_name = usuario.display_name
    criado_em = usuario.created_at.replace(tzinfo=timezone.utc).strftime('%d/%m/%Y as %H:%M:%S')
    entrou_servidor = usuario.joined_at.replace(tzinfo=timezone.utc).strftime('%d/%m/%Y as %H:%M:%S')
    TopRole = usuario.roles[-1].mention if len(usuario.roles) > 1 else "Nenhum"
    cargos = ', '.join([role.mention for role in usuario.roles[1:]]) or "Nenhum"

    embed_userinfo = discord.Embed(title=f'Userinfo - {user_name}', color=discord.Color.blurple())
    
    embed_userinfo.add_field(name='Nome', value=user_name, inline=True)
    embed_userinfo.add_field(name='ID', value=user_id, inline=True)
    embed_userinfo.add_field(name='Cargos', value=cargos, inline=False)
    embed_userinfo.add_field(name='Maior Cargo', value=TopRole, inline=True)
    embed_userinfo.add_field(name='Entrou no Discord', value=criado_em, inline=False)
    embed_userinfo.add_field(name='Entrou no Servidor', value=entrou_servidor, inline=False)
    
    # Define o avatar do usuário na embed
    embed_userinfo.set_thumbnail(url=usuario.display_avatar.url)
    embed_userinfo.set_footer(text=f"Informações solicitadas por {interaction.user}", icon_url=interaction.user.display_avatar.url)
    
    # Envia a embed como resposta
    await interaction.response.send_message(embed=embed_userinfo)
