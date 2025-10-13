"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Jan Kuděla
email: jochanan.jorgen@gmail.com
"""

import sys
import requests
from requests import get
from bs4 import BeautifulSoup

url = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
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

print(nazev_obce[6:])

volici_v_seznamu = parsovane_html_2.find_all("td")[3].get_text()
print(volici_v_seznamu)

vydane_obalky = parsovane_html_2.find_all("td")[4].get_text()
print(vydane_obalky)

platne_hlasy = parsovane_html_2.find_all("td")[7].get_text()
print(platne_hlasy)

strana = parsovane_html_2.find_all("td", {"class": "overflow_name"})
#print(strana)

strana_soupis = []
for a in strana:
    text = a.get_text(strip=True)
    strana_soupis.append(text)

print(strana_soupis)

strana_hlasy = parsovane_html_2.find_all("td", {"class": "cislo", "headers": "t1sa2 t1sb3"})
hlasy_soupis = []
for a in strana_hlasy:
    cislo = a.get_text(strip=True)
    hlasy_soupis.append(cislo)
print(hlasy_soupis) 