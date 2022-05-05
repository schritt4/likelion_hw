import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("충성충성^^7")

message["Subject"] = "멋사 대학 10기 전재병"
message["From"] = "royoet@gmail.com"
message["To"] = "ksjoon28@naver.com"

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

try:
    smtp.login("royoet@gmail.com", "password")
    smtp.send_message(message)
    smtp.quit()
    print("정상적으로 메일이 발송되었습니다.")
except: 
    print("메일 발송에 실패하였습니다.")