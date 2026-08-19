# Keylogger_Via_Email
Código para fins educativos e utilizado em ambiente de teste controlado, com VMs e máquinas prontas para uso do malware.

Versão inicial do Keylogger, com a ideia de capturar o conteúdo escrito pela vítima e ser enviada via SMTP do Google, através de uma conta gmail (Que necessariamente precisa estar verificada a um número de Telefone ou MFA2), pode funcionar também em segundo plano com o arquivo sendo executado em .pyw.

O código precisa estar em execução através de uma IDE, tanto na máquina do atacante (apenas executando deixando o código aberto para captura e envio de dados), quanto no da vítima.

As bibliotecas usadas foram:
- Python Documentation — https://docs.python.org/3/
- Cryptography (Fernet) — https://cryptography.io/
- pynput — https://pypi.org/project/pynput/
- smtplib — https://docs.python.org/3/library/smtplib.html
- pip - https://pip.pypa.io/en/stable/
- keyboard - https://pypi.org/project/keyboard/


# Ransoware Local
Código para fins educativos e utilizado em ambiente de teste controlado, com VMs e máquinas prontas para uso do malware.

Uma versão local de um ransoware que criptografa e descriptografa arquivos de forma simples, e que necessita de código rodando em aberto no PC da vítima para funcionar corretamente, não é tão discreto, porém pode funcionar também em segundo plano com o arquivo sendo executado em .pyw. 

As bibliotecas usadas foram:
- Python Documentation — https://docs.python.org/3/
- Cryptography (Fernet) — https://cryptography.io/
- pynput — https://pypi.org/project/pynput/
- pip - https://pip.pypa.io/en/stable/
- keyboard - https://pypi.org/project/keyboard/
