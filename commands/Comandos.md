# Comandos Slash

### Todos os comandos nesta pasta são comandos slash. Para que eles funcionem corretamente, é importante sincronizá-los com o servidor do Discord.

## O que são comandos slash ?
Comandos slash são aqueles que você usa com o formato `/comando`, o que facilita a utilização e torna os comandos mais acessíveis aos usuários. Eles aparecem automaticamente como sugestões no Discord, melhorando a experiência de uso.

## Configuração Inicial e Sincronização
Para que esses comandos estejam disponíveis para os usuários, é necessário sincronizá-los com o servidor. Isso significa que, após adicionar ou editar um comando, você precisa garantir que ele seja atualizado na lista de comandos slash do Discord.

## Como sincronizar os comandos
Ao iniciar o bot: No código do seu bot, o processo de sincronização geralmente é feito na função `on_ready` com `await bot.tree.sync()`. Certifique-se de que essa linha esteja no seu código para que, ao iniciar, todos os comandos slash sejam atualizados automaticamente.

## Se os comandos não aparecem:
- Verifique as permissões do bot, especialmente `applications.commands`.
- Confirme que o bot está rodando a versão correta do código e que `bot.tree.sync()` foi executado.

## O que você precisa saber
**Permissões:** Os comandos slash precisam que o bot tenha as permissões adequadas para serem registrados e usados.  
**Tempo de Atualização:** Pode levar alguns segundos para que o Discord atualize a lista de comandos.  
**Atualizações Locais e Globais:** Se você precisa que comandos estejam disponíveis em todos os servidores ou em apenas um servidor específico, ajuste a sincronização para guild (específico) ou global (todos).
