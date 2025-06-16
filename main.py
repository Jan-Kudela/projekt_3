"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Jan Kuděla
email: jochanan.jorgen@gmail.com
"""

import sys
import requests
from requests import get
from bs4 import BeautifulSoup

url = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101"
odpoved = requests.get(url)
if odpoved.status_code != 200:
    print("Chyba při načítání stránky:", odpoved.status_code)
    sys.exit(1)
    
parsovane_html = BeautifulSoup(odpoved.text, features="html.parser")

hledany_odkaz = parsovane_html.find_all("table", {"class": "table"})

number_list = []
for a in hledany_odkaz:
    hledany_a = a.find_all("a")
    for b in hledany_a:
        number = (b.get_text())
        if number.isdigit():
            number_list.append(number)

#hledane_cislo = hledany_odkaz.get_text()


#print(hledany_a[0].get_text())



print(number_list)
