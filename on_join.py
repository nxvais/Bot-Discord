#Modulos Necessarios

#import discord
#from discord.ext import commands

JoinLog = True  # Define se os logs de boas-vindas estão ativados
IdCanalRegras = 1300586361161519154  # Troque pelo ID do seu canal de regras

@bot.event
async def on_member_join(member: discord.Member):
    if JoinLog:
        # Obtém o canal onde as mensagens de boas-vindas serão enviadas
        ChatJoin = bot.get_channel(1300586361161519154)  # Troque pelo ID do seu canal de boas-vindas
        if ChatJoin is not None:
            if IdCanalRegras is not None:
                # Obtém o canal de regras
                CanalRegras = bot.get_channel(IdCanalRegras)

            embedJoin = discord.Embed(title=f'{member.display_name} | Seja Bem-vindo(a)')
            embedJoin.description = f'{member.display_name}! Estamos felizes por tê-lo conosco!'
            
            embedJoin.add_field(name='Membros', value=f'Você é o {member.guild.member_count}° Membro do Servidor!', inline=True)
            if IdCanalRegras is not None:
                embedJoin.add_field(name='Leia as Regras', value=f'Lembre-se de Ler as {CanalRegras.mention} para evitar ser Punido(a).', inline=True)  # Troque "CanalRegras" pelo seu canal de regras
            
            embedJoin.add_field(name='Equipe', value='Caso precise de ajuda, pode chamar a nossa equipe de moderação!', inline=True)
            embedJoin.add_field(name='Aproveite!', value='Estamos aqui para nos divertir e fazer novas amizades!', inline=True)

            embedJoin.set_thumbnail(url=member.display_avatar.url)
            embedJoin.color = discord.Colour.dark_purple()
            
            # Envia a menção ao novo membro e o embed de boas-vindas
            await ChatJoin.send(member.mention)  # Envia uma mensagem mencionando o novo membro
            await ChatJoin.send(embed=embedJoin)  # Envia o embed de boas-vindas
            
        else:
            # Mensagem de erro se o canal para logs de boas-vindas não for encontrado
            print('O Canal para as Logs de Boas Vindas não foi setado.')
            print('Troque o "ChatJoin" para o ID do Canal que deseja enviar a Mensagem')
