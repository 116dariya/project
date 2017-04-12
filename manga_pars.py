import requests 
from bs4 import BeautifulSoup
url = "http://manga-sushi.kz/menu/rolls_"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
rows = soup.select("div.good-item")
for item in rows:
	data_id = item['data-id']
	name = item.select("div.good-item-title")[0].text
	price = item.select("div.good-item-price")[0].text
	desc = item.select("div.good-item-desc div.good-item-in")[0].text
	print("%s%s" %(data_id,name))
	print(desc)
	print((price).replace(' ', ''))
	q = item.select("span.more")
	for i in q:
		num = i["data-rolls_num"]
		print("Количество роллов в одном сете:" + num)
		break


urrl = "http://manga-sushi.kz/menu/sushi"
t = requests.get(urrl)
html = t.text
souup = BeautifulSoup(html, "html.parser")
roows = souup.select("div.good-item")
for item in roows:
	data_id = item['data-id']
	name = item.select("div.good-item-title")[0].text
	price = item.select("div.good-item-price")[0].text
	desc = item.select("div.good-item-desc div.good-item-in")[0].text
	print("%s%s" %(data_id,name))
	print(desc)
	print((price).replace(' ', ''))
	print("Количество суши в одном сете:1")

