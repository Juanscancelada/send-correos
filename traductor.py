import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

your_email = "cancelada2003@gmail.com"
your_password = "sffd wucj yuet lgby"

recipent = "rafael.cancelada@gmail.com"

message = MIMEMultipart()
message["From"] = your_email
message["To"] = recipent
message["Subject"] = "Email de ejemplo"

body = "Este es un texto de ejemplo para el proyecto de enviar correos con python"
message.attach(MIMEText(body, "plain"))

#llamar al servidor para logearnos en gmail y el puerto (587)
smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls()
#logeo de la cuenta para poder mandar el correo
smtp_server.login(your_email, your_password)

smtp_server.sendmail(your_email, recipent, message.as_string())
smtp_server.quit()
print("Email enviado")