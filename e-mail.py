import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

# Função para enviar o e-mail
def enviar_email():
    # Definições fixas
    remetente = "frank.melo.wal@gmail.com"  # Coloque o seu e-mail
    senha = "fgkbjvmjncmwtivp"  # Coloque sua senha ou senha de app
    destinatario = "crislaynegualberto70@gmail.com"  # E-mail do destinatário
    assunto = "Uma mensagem de amor"

    # Corpo do e-mail com a mensagem de amor
    corpo = "Te amo de coração e alma. Você é tudo para mim. 💖"

    # Configurações do servidor SMTP do Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Criar a mensagem do e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto

    # Adicionar o corpo do e-mail
    mensagem.attach(MIMEText(corpo, 'plain'))

    try:
        # Conectar ao servidor SMTP e enviar o e-mail
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Iniciar a conexão segura
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, mensagem.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Falha ao enviar e-mail: {e}")
    finally:
        server.quit()

# Agendar o envio do e-mail todos os dias às 22:00 (substitua pelo horário desejado)
schedule.every().day.at("20:46").do(enviar_email)

# Manter o script em execução para cumprir o agendamento
while True:
    schedule.run_pending()
    time.sleep(1)