@bot.tree.command(description='Veja meu ping Atual!')
async def ping(interaction: discord.Interaction):
    user = interaction.user
    ping = bot.latency * 1000
    embedPing = discord.Embed(title='Ping, 🏓 Pong!')
    embedPing.description = f'📡 | Meu ping Atual é de {ping:.0f}ms'
    embedPing.colour = discord.Colour.orange()
    
    await interaction.response.send_message(embed=embedPing)
