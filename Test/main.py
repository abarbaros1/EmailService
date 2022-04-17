import smtplib, ssl
smtp_server = 'smtp.gmail.com'
port = 465

sender = 'python.project.tekwill@gmail.com'
password = input('Input your password here')

receiver = 'manevairina.86@mail.ru'
message = """"\
From: {}
To: {}
Subject: Hi There!
This message is from Python
  """.format(sender, receiver)

context = ssl.create_default_context()


with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)

# try:
#     server = smtplib.SMTP(smtp_server,port)
#     server.ehlo()
#     server.starttls(context=context)
#     server.ehlo()
#     server.login(sender, password)
#     print('It worked')
# except Exception as e:
#     print(e)
# finally:
#     server.quit()
