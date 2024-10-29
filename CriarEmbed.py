#Modulos necessarios
# import discord
# from discord.ext import commands
# from discord.ui import Button, View, Select, Modal, TextInput



@bot.tree.command(description='Abre um Painel de Criação de Embed')
async def criarembed(interact: discord.Interaction):
    embed_criador = discord.Embed(title='Esse é o seu Embed')
    embed_criador.description = 'Você pode editar cada elemento, clique nos Botões e Digite os Valores.'
    embed_criador.set_footer(text='Rodapé/Footer (Opcional)')
    
    embed_final = discord.Embed(title='Você não definiu um titulo...')
    
    botaoTitulo = Button(label='Titulo', style=discord.ButtonStyle.secondary)
    botaoDescr = Button(label='Descrição', style=discord.ButtonStyle.secondary)
    botaoFooter = Button(label='Footer', style=discord.ButtonStyle.secondary)
    botaoImagem = Button(label='Imagem', style=discord.ButtonStyle.secondary)
    botaoThumb = Button(label='Thumbnail', style=discord.ButtonStyle.secondary)
    botaoFinalizar = Button(label='Concluir', style=discord.ButtonStyle.success)
    
    SelectMenuCor = Select(placeholder='Selecione uma Cor')
    opçoes = [discord.SelectOption(label='Vermelho', value='1'), 
              discord.SelectOption(label='Azul', value='2'),
              discord.SelectOption(label='Verde', value='3'),
              discord.SelectOption(label='Amarelo', value='4'),
              discord.SelectOption(label='Branco', value='5'),
              discord.SelectOption(label='Preto', value='6'),
              discord.SelectOption(label='Escolher Cor Hexadecimal', value='7')]
    SelectMenuCor.options = opçoes
    
    
    view = View()
    view.add_item(botaoTitulo)
    view.add_item(botaoDescr)
    view.add_item(botaoFooter)
    view.add_item(botaoImagem)
    view.add_item(botaoThumb)
    view.add_item(SelectMenuCor)
    view.add_item(botaoFinalizar)
    
    await interact.response.send_message(embed=embed_criador, view=view, ephemeral=True)
    
    async def botaoTitulo_callback(interaction):
        FormTitulo = Modal(title='Titulo do Embed')
        TituloSet = TextInput(label='Titulo', max_length=256, min_length=1, placeholder='Esse é o seu Titulo',required=True)
        FormTitulo.add_item(TituloSet)
        
        async def on_submit_Titulo(interaction: discord.Interaction):
            embed_final.title = f'{TituloSet}'
            embed_criador.title = f'{TituloSet}'
            await interaction.response.edit_message(embed=embed_criador)
            await interaction.followup.send(f'Você setou o **Titulo** do Embed para "{TituloSet}"', ephemeral=True)
        
        FormTitulo.on_submit = on_submit_Titulo
        await interaction.response.send_modal(FormTitulo)
        
        
        
        
    async def botaoDescr_callback(interaction):
        FormDescr = Modal(title='Descrição do Embed')
        DescrSet = TextInput(label='Descrição', max_length=4000, min_length=1, placeholder='Essa é a Minha Descrição, Ok ?',style=discord.TextStyle.long, required=True)
        FormDescr.add_item(DescrSet)
        
        async def on_submit_Descr(interaction: discord.Interaction):
            embed_criador.description = f'{DescrSet}'
            embed_final.description = f'{DescrSet}'
            await interaction.response.edit_message(embed=embed_criador)
            await interaction.followup.send(f'Você setou a **Descrição** do Embed para "{DescrSet}"', ephemeral=True)
        
        FormDescr.on_submit = on_submit_Descr
        await interaction.response.send_modal(FormDescr)
        
        
        
        
    async def botaoFooter_callback(interaction):
        FormFooter = Modal(title='Rodapé do Embed')
        FooterSet = TextInput(label='Rodapé/Footer', max_length=2048, min_length=1, placeholder='Rodapé... apenas isso',required=False)
        FormFooter.add_item(FooterSet)
        
        async def on_submit_Footer(interaction: discord.Interaction):
            if FooterSet.value != None:
                embed_criador.set_footer(text=f'{FooterSet}')
                embed_final.set_footer(text=f'{FooterSet}')
                await interaction.response.edit_message(embed=embed_criador)
                await interaction.followup.send(f'Você setou o **Rodapé** do Embed para "{FooterSet}"', ephemeral=True)
        
        FormFooter.on_submit = on_submit_Footer
        await interaction.response.send_modal(FormFooter)
        
        
    async def botaoImagem_callback(interaction):
        FormImg = Modal(title='Imagem do Embed (URL)')
        ImgSet = TextInput(label='URL', max_length=4000, min_length=1, placeholder='https://www.ImagemMuitoDahora.novais.com.br',required=False)
        FormImg.add_item(ImgSet)
        
        async def on_submit_image(interaction: discord.Interaction):
            if ImgSet.value:
                embed_criador.set_image(url=ImgSet.value)
                embed_final.set_image(url=ImgSet.value)
                await interaction.response.edit_message(embed=embed_criador)
        
        FormImg.on_submit = on_submit_image
        await interaction.response.send_modal(FormImg)
        
        
    async def botaoThumb_callback(interaction):
        FormThumb = Modal(title='Thumbnail do Embed (URL)')
        ThumbSet = TextInput(label='URL', max_length=4000, min_length=1, placeholder='https://www.ThumbnailMuitoDahora.Novais.com.br',required=False)
        FormThumb.add_item(ThumbSet)
        
        async def on_submit_thumb(interaction: discord.Interaction):
            if ThumbSet.value:
                embed_criador.set_thumbnail(url=ThumbSet.value)
                embed_final.set_thumbnail(url=ThumbSet.value)
                await interaction.response.edit_message(embed=embed_criador)
        
        FormThumb.on_submit = on_submit_thumb
        await interaction.response.send_modal(FormThumb)
        
        
    async def Select_Cores(interaction: discord.Interaction):
        escolha = interaction.data['values'][0]
        
        cores = {
        '1': (discord.Colour.red(), 'Vermelho'), #Vermelho
        '2': (discord.Colour.blue(), 'Azul'), #Azul
        '3': (discord.Colour.green(), 'Verde'), #Verde
        '4': (discord.Colour.gold(), 'Amarelo'),  # Amarelo
        '5': (discord.Colour.from_rgb(255, 255, 255), 'Branco'),  # Branco
        '6': (discord.Colour.from_rgb(0, 0, 0), 'Preto')  # Preto
        }

        # Define a cor com base na escolha
        if escolha in cores:
            embed_final.color, cor_nome = cores[escolha]
            embed_criador.color = embed_final.color
            await interaction.response.edit_message(embed=embed_criador)
            await interaction.followup.send(f'Você setou a **Cor** do Embed para "{cor_nome}"', ephemeral=True)

    
            
        elif escolha == '7': #Hexadecimal
            FormHex = Modal(title='Sistema de Cores no Embed')
            Hexadecimal = TextInput(label='Cor em HEX', placeholder="FF0000", min_length=6, max_length=6, required=True)
            FormHex.add_item(Hexadecimal)

            async def on_submit_Hex(interaction: discord.Interaction):
                Cor = Hexadecimal.value  # Pega o valor do campo de entrada
                ValorCor = int(Cor, 16)
                embed_final.color = ValorCor
                embed_criador.color = ValorCor
                await interaction.response.edit_message(embed=embed_criador)
                await interaction.followup.send(f'Você setou a **Cor** do Embed para "{Cor}"', ephemeral=True)
                
            FormHex.on_submit = on_submit_Hex
            await interaction.response.send_modal(FormHex)
            
        
        
        
        
    async def botaoFinalizar_callback(interaction):
        await interaction.channel.send(embed=embed_final)
        await interaction.response.send_message('O seu Embed foi Finalizado com Sucesso!', ephemeral=True)

        

        
    botaoTitulo.callback = botaoTitulo_callback
    botaoDescr.callback = botaoDescr_callback
    botaoFooter.callback = botaoFooter_callback
    botaoImagem.callback = botaoImagem_callback
    botaoThumb.callback = botaoThumb_callback
    botaoFinalizar.callback = botaoFinalizar_callback
    SelectMenuCor.callback = Select_Cores
