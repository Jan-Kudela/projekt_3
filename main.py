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
#obsahuje čísla obcí, které jsou v odkazu
for a in hledany_odkaz:
     hledany_a = a.find_all("a")
     for b in hledany_a:
        number = (b.get_text())
        if number.isdigit():
            number_list.append(number)

#print(number_list)


url_2 = url[:37] + "311"+ url[39:59] +"xobec=" + number_list[0] + "&xvyber=" + url[-4:]
#url pro vybranou obec

odpoved_2 = requests.get(url_2)
if odpoved_2.status_code != 200:
    print("Chyba při načítání stránky:", odpoved_2.status_code)
    sys.exit(1)

parsovane_html_2 = BeautifulSoup(odpoved_2.text, features="html.parser")
nazev_obce = parsovane_html_2.find_all("h3")[2].get_text()
#print(nazev_obce)

volici_v_seznamu = parsovane_html_2.find_all("tbody")