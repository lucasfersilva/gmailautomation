import ezgmail , os


def envia_email():

    Destinatarios = input("Para: ")
    Assunto = input('Assunto: ')
    Mensagem = input('Digite sua Mensagem: ')
    ezgmail.send(Destinatarios, Assunto, Mensagem)
    print('E-mail Enviado com sucesso')


def le_email():

    unreadThreads = ezgmail.unread(maxResults=30)  # List of GmailThread objects.
    ezgmail.summary(unreadThreads)


Mensagem = input('Digite 1 para ler seus emails não lidos '
                 '2 para enviar um E-mail: ')
if Mensagem == '1':
    le_email()
elif Mensagem == '2':
    envia_email()



