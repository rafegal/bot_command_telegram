# bot_command_telegram

Orquestra comandos enviados para seu bot no Telegram.
Os comandos são executados através de scripts Python.
Cada script irá possui um valor de entrada que é o comando, o script também pode receber um parâmetro junto com o comando.

Os comandos são inseridos na base de dados.
Essa projeto foi desenvolvido na [Live de Python](https://youtu.be/xljES_-IbLA), foi feita algumas atualizações, mas a base é a mesma, assistir a live é suficiente para entimento do projeto.

O token do seu bot no telegram deve ser armazenado na variável de ambiente TOKEN_TELEGRAM. Também é possível criar um arquivo .env na raiz do projeto e criar essa variável dentro deste arquivo, ficando da seguinte forma:

```TOKEN_TELEGRAM=<TOKEN>```

Sem informar o token a aplicação não arranca.
Também é possível parametrizar a mensagem de exceção para quando ocorre um erro no processamento. A mensagem de exceção enviado para o usuário é buscado da variável de ambiente EXCEPTION_MESSAGE. Essa variável não é obrigatório, pois ela possui uma valor default. Ambos os parâmetros se encontram no arquivo settings.