#Modulos Necessários
#from captcha.image import ImageCaptcha
#import discord
#from discord.ui import *

# Comando principal do bot que cria um painel de verificação interativo
@bot.tree.command(description='Cria um painel interativo para os usuários se Verificarem no servidor.')  
async def painelverify(interaction: discord.Interaction):
    # Verifica se o usuário que executou o comando tem permissão de administrador
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message('Você não tem a permissão de **ADMINISTRADOR** para utilizar esse Botão.', ephemeral=True)
        return  # Se não tiver permissão, retorna e não executa mais nada
    
    # Criação do embed para o painel de verificação
    embedVerify = discord.Embed(title='Painel de Verificação', description='Clique no botão abaixo para iniciar a verificação.', color=discord.Color.dark_blue())
    
    # Criação do botão que vai iniciar a verificação
    BotãoVerify = Button(label='Verifique-se', style=discord.ButtonStyle.secondary, emoji='🔑')
    
    # Criação de uma view (uma coleção de componentes interativos) para o primeiro botão
    PrimeiraView = View(timeout=None)
    PrimeiraView.add_item(BotãoVerify)
    
    # Envia o painel de verificação (com o embed e o botão) para o canal onde o comando foi executado
    await interaction.response.send_message(embed=embedVerify, view=PrimeiraView)
    
    # Função de callback que é chamada quando o botão de verificação é pressionado
    async def verify_callback(interaction):
        # Geração do captcha usando a biblioteca ImageCaptcha
        imagem = ImageCaptcha(width=280, height=90)  
        captcha_text = ''.join(choices(string.ascii_letters + string.digits, k=6))  # Gera um código de 6 caracteres aleatórios

        # Gera a imagem do captcha com o texto aleatório gerado
        data = imagem.generate(captcha_text)
        
        # Criação do botão para o usuário clicar e responder ao captcha
        BotãoInputCaptcha = Button(label='Responder Captcha', style=discord.ButtonStyle.secondary, emoji='🔑')
        
        # Criação de uma nova view para o botão de resposta do captcha
        SegundaView = View(timeout=None)
        SegundaView.add_item(BotãoInputCaptcha)
     
        # Envia o captcha como imagem junto com o botão de resposta
        await interaction.response.send_message(file=discord.File(data, 'captcha.png'), view=SegundaView, ephemeral=True)  
        
        # Função de callback para quando o usuário clicar no botão de resposta do captcha
        async def input_captcha_callback(interaction):
            # Criação de um modal (janela interativa) para o usuário digitar o captcha
            ModalCaptcha = Modal(title='Digite o Captcha')
            InputCaptcha = TextInput(label='Digite o Captcha (6 Dígitos)', placeholder='Digite o Captcha', style=discord.TextInputStyle.short, max_length=6, min_length=6, required=True)
            
            # Adiciona o campo de entrada de texto ao modal
            ModalCaptcha.add_item(InputCaptcha)
            
            # Função que será chamada quando o usuário enviar o modal
            async def on_submit_captcha(interaction):
                # ID do cargo que será atribuído ao usuário se o captcha for correto
                CargoID = 1300592091415449621 
                
                # Verifica se o texto digitado pelo usuário corresponde ao texto gerado do captcha
                if InputCaptcha.value.lower() == captcha_text.lower():
                    # Se o captcha estiver correto, envia uma mensagem de sucesso
                    EmbedSucesso = discord.Embed(title='Captcha Correto', color=discord.Colour.from_rgb(0, 255, 0))
                    EmbedSucesso.add_field(name='Captcha Correto', value='Você foi verificado com sucesso\nVocê terá acesso aos outros canais em Breve...', inline=False)
                    
                    # Obtém o cargo com o ID definido e atribui ao usuário
                    cargo = interaction.guild.get_role(CargoID)
                    await interaction.response.send_message(embed=EmbedSucesso, ephemeral=True)
                    
                    # Atribui o cargo ao usuário
                    await interaction.user.add_roles(cargo)
                    
                else:
                    # Se o captcha estiver errado, envia uma mensagem de erro
                    EmbedErro = discord.Embed(title='Erro', color=discord.Colour.from_rgb(255, 0, 0))
                    EmbedErro.add_field(name='Captcha Errado', value='Tente Novamente...', inline=False)
                    
                    # Envia a mensagem de erro
                    await interaction.response.send_message(embed=EmbedErro, ephemeral=True)
            
            # Atribui a função de envio para o modal
            ModalCaptcha.on_submit = on_submit_captcha
            # Exibe o modal para o usuário preencher
            await interaction.response.send_modal(ModalCaptcha)
        
        # Associa o callback ao botão de resposta do captcha
        BotãoInputCaptcha.callback = input_captcha_callback

    # Associa a função de callback ao primeiro botão de verificação
    BotãoVerify.callback = verify_callback
