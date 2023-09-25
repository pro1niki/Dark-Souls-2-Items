import requests
from bs4 import BeautifulSoup
import json
import operator
import datetime

items = ["Ultra Greatswords", "Rings", "Greatswords",
         "Daggers", "Straight Swords", "Curved Swords",
         "Katanas", "Curved Greatswords", "Piercing Swords",
         "Axes", "Great Axes", "Hammers", "Great Hammers",
         "Fist Weapons", "Spears", "Halberds", "Lances",
         "Reapers", "Twinblades", "Whips", "Bows", "Greatbows",
         "Crossbows", "Flames", "Chimes", "Staves"]
links = []

data = []
fl = "https://darksouls2.wiki.fextralife.com/file/Dark-Souls-2/"

def getItems(item):
    itemsJson = []
    req = requests.get('https://darksouls2.wiki.fextralife.com/'+item)
    if req.status_code == 200:
        print('Successful Request!')
    content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    i = 0
    for tr in soup.find_all('tr'):
        tr = tr.td
        tr = str(tr)
        tr = tr.replace("title=\"", "[")
        tr = tr.replace("\"/>", "[")
        tr = tr.split("[")
        if tr != "None":
            if tr[0] != "None":
                if len(tr) > 1:
                    if tr[1].find("icon") != -1:
                        continue
                    final = tr[1].find(".png")
                    if final != -1:
                        final += 4
                        tr[1] = tr[1][0:final]
                        l = fl + tr[1]
                        links.append(l)
                        sword = tr[1].replace("_", " ")
                        sword = sword.replace(".png", "")
                        itemsJson.append({
                            "item": sword,
                            "imgLink": l
                        })
                        print(sword)
    item = item.replace("+", " ")
    data.append({item: itemsJson})
for item in items:
    item = item.replace(" ", "+")
    getItems(item)

import json
with open('items.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)