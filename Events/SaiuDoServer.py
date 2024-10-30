#Modulos Necessarios

#import discord
#from discord.ext import commands

# Configurações
LeaveLog = True  # Define se os logs de saída estão ativados
IdCanalSaida = 1300586361161519154  # Troque pelo ID do canal onde deseja enviar as mensagens de saída

@bot.event
async def on_member_remove(member: discord.Member):
    # Verifica se os logs de saída estão ativados e o canal está configurado
    if LeaveLog:
        ChatSaida = bot.get_channel(IdCanalSaida)
        if ChatSaida is not None:
            # Cria o embed para a mensagem de saída
            embedLeave = discord.Embed(title=f"{member.display_name} saiu do servidor")
            embedLeave.description = f"{member.display_name} não faz mais parte do servidor."
            embedLeave.add_field(name="Membros", value=f"Agora temos {member.guild.member_count} membros.", inline=True)
            embedLeave.set_thumbnail(url=member.display_avatar.url)
            embedLeave.color = discord.Colour.red()

            # Envia o embed de saída no canal definido
            await ChatSaida.send(embed=embedLeave)
        else:
            # Mensagem de erro se o canal de saída não for encontrado
            print("O Canal para logs de saída não foi configurado corretamente.")
            print("Certifique-se de definir 'IdCanalSaida' com o ID do canal desejado.")
