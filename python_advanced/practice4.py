import smtplib
from email.message import EmailMessage
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")


message = EmailMessage()
message.set_content("충성충성^^7")

message["Subject"] = "멋사 대학 10기 전재병"
message["From"] = "royoet@gmail.com"
message["To"] = "ksjoon28@naver.com"

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

smtp.login("royoet@gmail.com", "password")
sendEmail("ksjoon28@naver.com")
smtp.quit()