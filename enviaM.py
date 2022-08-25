from email.message import EmailMessage
import ssl
import smtplib

emailSender = 'viniciuswebscrp@gmail.com'
emailReceiver ='viniciusag626@gmail.com'
emailPass = 'wgwggeoythwlcedj'


em = EmailMessage()

def criaMsg(arq):
    em.set_content('Data scrapped - kabum teclados gamers')
    em['Subject'] = "Envio dos dados"
    em['From'] = emailSender
    em['To'] = emailReceiver
    with open(arq, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    em.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    return


context = ssl.create_default_context()


def envia(arq):
    criaMsg(arq)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPass)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())
    return
