# Keylogger_Via_Email
Versão inicial do Keylogger, com a ideia de capturar o conteúdo escrito pela vítima e ser enviada via SMTP do Google, através de uma conta gmail (Que necessariamente precisa estar verificada a um número de Telefone ou MFA2).

O código precisa estar em execução através de uma IDE, tanto na máquina do atacante (apenas executando deixando o código aberto para captura e envio de dados), quanto no da vítima.

As bibliotecas usadas foram:
- Python Documentation — https://docs.python.org/3/
- Cryptography (Fernet) — https://cryptography.io/
- pynput — https://pypi.org/project/pynput/
- smtplib — https://docs.python.org/3/library/smtplib.html
