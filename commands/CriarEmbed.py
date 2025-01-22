#Modulos necessarios
# import discord
# from discord.ext import commands
# from discord.ui import Button, View, Select, Modal, TextInput

@bot.tree.command(name='criarembed', description='Cria uma embed personalizada para ser enviada no servidor.')
async def criarembed(interaction: discord.Interaction):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message('Você não tem a permissão de **ADMINISTRADOR** para utilizar esse Comando.', ephemeral=True)
        return
        
    embedPadrão = discord.Embed(title='Personalize Sua Embed', description='Edite os parametros abaixo que desejar.', color=discord.Colour.from_rgb(255, 255, 255))
    
    BotãoTitulo = Button(label='Titulo', style=discord.ButtonStyle.primary, emoji='📝')
    BotãoDescricao = Button(label='Descrição', style=discord.ButtonStyle.primary, emoji='📝')
    BotãoCor = Button(label='Cor', style=discord.ButtonStyle.primary, emoji='🎨')
    BotãoAutor = Button(label='Autor', style=discord.ButtonStyle.primary, emoji='👤')
    BotãoImagemThumb = Button(label='Imagem e Thumbnail', style=discord.ButtonStyle.primary, emoji='📸')
    BotãoRodapé = Button(label='Rodapé', style=discord.ButtonStyle.primary, emoji='📝')
    BotãoExportar = Button(label='Exportar Json', style=discord.ButtonStyle.secondary, emoji='📝')
    BotãoImportar = Button(label='Importar Json', style=discord.ButtonStyle.secondary, emoji='📝')
    BotãoEnviar = Button(label='Enviar Embed', style=discord.ButtonStyle.success, emoji='✉️')
    
    viewEmbed = View(timeout=None)
    viewEmbed.add_item(BotãoTitulo)
    viewEmbed.add_item(BotãoDescricao)
    viewEmbed.add_item(BotãoCor)
    viewEmbed.add_item(BotãoAutor)
    viewEmbed.add_item(BotãoImagemThumb)
    viewEmbed.add_item(BotãoRodapé)
    viewEmbed.add_item(BotãoExportar)
    viewEmbed.add_item(BotãoImportar)
    viewEmbed.add_item(BotãoEnviar)
    
    await interaction.response.send_message(embed=embedPadrão, view=viewEmbed, ephemeral=True)
    
    embed_states = {}
    
    def get_embed(interaction):
        if interaction.message.id not in embed_states:
            embed_states[interaction.message.id] = discord.Embed(
                title="Personalize Sua Embed",
                description="Edite os parâmetros abaixo que desejar.",
                color=discord.Color.blue()
            )
        return embed_states[interaction.message.id]

    # Função para definir a embed atualizada
    def set_embed(interaction, embed):
        embed_states[interaction.message.id] = embed
    
    async def titulo_callback(interaction):
        ModalTitulo = Modal(title='Digite o Titulo da Embed')
        InputTitulo = TextInput(label='Digite o Titulo', placeholder='Digite o Titulo', style=discord.TextStyle.short, required=False)
        
        ModalTitulo.add_item(InputTitulo)
        
        async def on_submit_titulo(interaction):
            embedPadrão = get_embed(interaction)
            embedPadrão.title = InputTitulo.value
            set_embed(interaction, embedPadrão)
            await interaction.response.edit_message(embed=embedPadrão, view=viewEmbed)
            
        ModalTitulo.on_submit = on_submit_titulo
        await interaction.response.send_modal(ModalTitulo)
        
    BotãoTitulo.callback = titulo_callback
    
    async def descricao_callback(interaction):
        ModalDescricao = Modal(title='Digite a Descricao da Embed')
        InputDescricao = TextInput(label='Digite a Descricao', placeholder='Digite a Descricao', style=discord.TextStyle.short, required=False)
        
        ModalDescricao.add_item(InputDescricao)
        
        async def on_submit_descricao(interaction):
            embedPadrão = get_embed(interaction)
            embedPadrão.description = InputDescricao.value
            set_embed(interaction, embedPadrão)
            await interaction.response.edit_message(embed=embedPadrão, view=viewEmbed)
            
        ModalDescricao.on_submit = on_submit_descricao
        await interaction.response.send_modal(ModalDescricao)
        
    BotãoDescricao.callback = descricao_callback
    
    async def cor_callback(interaction):
        ModalCor = Modal(title='Digite a Cor da Embed')
        InputCor = TextInput(label='Digite a Cor', placeholder='Digite a Cor', style=discord.TextStyle.short, required=False)
        
        ModalCor.add_item(InputCor)
        
        async def on_submit_cor(interaction):
            embedPadrão = get_embed(interaction)
            embedPadrão.color = discord.Colour.from_rgb(int(InputCor.value[0:2], 16), int(InputCor.value[2:4], 16), int(InputCor.value[4:6], 16))
            set_embed(interaction, embedPadrão)
            await interaction.response.edit_message(embed=embedPadrão, view=viewEmbed)
            
        ModalCor.on_submit = on_submit_cor
        await interaction.response.send_modal(ModalCor)
        
    BotãoCor.callback = cor_callback
    
    async def autor_callback(interaction):
        ModalAutor = Modal(title='Digite o Autor da Embed')
        TextAutor = TextInput(label='Digite o Texto do Autor', placeholder='Digite o Autor', style=discord.TextStyle.short, required=False)
        UrlAutor = TextInput(label='Digite a URL do Autor', placeholder='Digite a URL do Autor', style=discord.TextStyle.short, required=False)
        
        ModalAutor.add_item(TextAutor)
        ModalAutor.add_item(UrlAutor)
        
        async def on_submit_autor(interaction):
            embedPadrão = get_embed(interaction)
            embedPadrão.set_author(name=TextAutor.value)
            if UrlAutor.value:
                embedPadrão.set_author(url=UrlAutor.value)
            set_embed(interaction, embedPadrão)
            await interaction.response.edit_message(embed=embedPadrão, view=viewEmbed)
            
        ModalAutor.on_submit = on_submit_autor
        await interaction.response.send_modal(ModalAutor)
        
    BotãoAutor.callback = autor_callback
    
    async def imagemANDthumb_callback(interaction):
        ModalImagem = Modal(title='Digite as Imagens da Embed')
        InputImagem = TextInput(label='Digite a URL da Imagem', placeholder='Digite a URL da Imagem', style=discord.TextStyle.short, required=False)
        InputThumb = TextInput(label='Digite a URL da Thumbnail', placeholder='Digite a URL da Thumbnail', style=discord.TextStyle.short, required=False)
        
        ModalImagem.add_item(InputImagem)
        ModalImagem.add_item(InputThumb)
        
        async def on_submit_imagem(interaction):
            embedPadrão = get_embed(interaction)
            if InputImagem.value:
                embedPadrão.set_image(url=InputImagem.value)
            if InputThumb.value:
                embedPadrão.set_thumbnail(url=InputThumb.value)
            set_embed(interaction, embedPadrão)
            await interaction.response.edit_message(embed=embedPadrão, view=viewEmbed)
            
        ModalImagem.on_submit = on_submit_imagem
        await interaction.response.send_modal(ModalImagem)
        
    BotãoImagemThumb.callback = imagemANDthumb_callback
        
    async def rodapé_callback(interaction):
        ModalRodapé = Modal(title='Digite o Rodapé da Embed')
        InputRodapé = TextInput(label='Digite o Texto do Rodapé', placeholder='Digite o Texto do Rodapé', style=discord.TextStyle.short, required=False)
        
        ModalRodapé.add_item(InputRodapé)
        
        async def on_submit_rodapé(interaction):
            embedPadrão = get_embed(interaction)
            embedPadrão.set_footer(text=InputRodapé.value)
            set_embed(interaction, embedPadrão)
            await interaction.response.edit_message(embed=embedPadrão, view=viewEmbed)
            
        ModalRodapé.on_submit = on_submit_rodapé
        await interaction.response.send_modal(ModalRodapé)
        
    BotãoRodapé.callback = rodapé_callback
    
    async def exportar_callback(interaction): 
        jsonEmbed = json.dumps(embedPadrão.to_dict())
        await interaction.response.send_message(jsonEmbed, ephemeral=True)
        
    BotãoExportar.callback = exportar_callback
    
    async def importar_callback(interaction):
        ModalImportar = Modal(title="Importar JSON")
        InputImportar = TextInput(
            label="Importar JSON",
            placeholder="Cole o JSON aqui",
            style=discord.TextStyle.long,
            required=True,
        )
        ModalImportar.add_item(InputImportar)

        async def on_submit_importar(interaction):
            try:
                jsonEmbed = json.loads(InputImportar.value)
                embed = discord.Embed.from_dict(jsonEmbed)
                set_embed(interaction, embed)
                await interaction.response.edit_message(embed=embed, view=viewEmbed)
            except Exception as e:
                await interaction.response.send_message(
                    f"Erro ao importar JSON: {e}", ephemeral=True
                )

        ModalImportar.on_submit = on_submit_importar
        await interaction.response.send_modal(ModalImportar)

    BotãoImportar.callback = importar_callback
    
    async def enviar_callback(interaction):
        embedPadrão = get_embed(interaction)
        if embedPadrão.title == 'Personalize Sua Embed':
            await interaction.response.send_message('Você não editou o Titulo da Embed', ephemeral=True)
            return
        elif embedPadrão.description == 'Edite os parametros abaixo que desejar.':
            await interaction.response.send_message(' você não editou a Descricao da Embed', ephemeral=True)
            return
        
        channel = interaction.channel
        await channel.send(embed=embedPadrão)
        await interaction.response.send_message('Embed Enviado', ephemeral=True)
    
    BotãoEnviar.callback = enviar_callback
