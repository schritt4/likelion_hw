import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://music.bugs.co.kr/chart"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1
results = soup.findAll("p", "title")

with open("practice1.txt", "w") as practice1:
    practice1.write(str(datetime.today())+"의 벅스 실시간 차트입니다.\n")
    for result in results:
        practice1.write(str(rank)+ " 위: "+result.get_text()+ "\n")
        rank += 1 