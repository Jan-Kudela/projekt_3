"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Jan Kuděla
email: jochanan.jorgen@gmail.com
"""

import sys
import requests
from requests import get
#from urllib.parse import urlparse, parse_qs, url_encode,
from bs4 import BeautifulSoup
import csv
import subprocess

def parsovani_html(url):
    odpoved = requests.get(url)
    if odpoved.status_code != 200:
        print("Chyba při načítání stránky:", odpoved.status_code)
        sys.exit(1)
    else:   
        parsovane_html = BeautifulSoup(odpoved.text, features="html.parser")

        return parsovane_html


def parsovani_cisel_obci(parsovane_html):
    """vrací list čísel obcí"""
    hledany_odkaz = parsovane_html.find_all("table", {"class": "table"})

    cisla_obci = []
    #obsahuje čísla obcí, které jsou v odkazu
    for a in hledany_odkaz:
        hledany_a = a.find_all("a")
        for b in hledany_a:
            number = (b.get_text())
            if number.isdigit():
                cisla_obci.append(number)

    return (cisla_obci)


def ziskani_url2(url, cisla_vsech_obci, index):
    url_2 = url[:37] + "311"+ url[39:59] +"xobec=" + cisla_vsech_obci[index] + "&xvyber=" + url[-4:]
    return url_2
#url pro vybranou obec


def parsovani_html2(url_2):
    odpoved_2 = requests.get(url_2)
    if odpoved_2.status_code != 200:
        print("Chyba při načítání stránky:", odpoved_2.status_code)
        sys.exit(1)

    else:
        parsovane_html_2 = BeautifulSoup(
            odpoved_2.text, features="html.parser"
            )

        return parsovane_html_2
    

def nazvy_obci(html):

    obce_soupis = []
    radky = html.find_all("tr")
    print(radky)
    for r in radky:
        td = r.find_all("td")
        if not td:
            continue
        
        nazev = td[1].get_text(strip=True)
        if not nazev:
            continue

        obce_soupis.append(nazev)

    return obce_soupis

##inner > div:nth-child(2) > table > tbody > tr:nth-child(24) > td:nth-child(2) > a

def volici(html):
    volici_v_seznamu = html.find_all("td")[3].get_text()
    return volici_v_seznamu


def obalky(html):
    vydane_obalky = html.find_all("td")[4].get_text()
    return vydane_obalky


def platne_hlasy(html):
    platne_hl = html.find_all("td")[7].get_text()
    return platne_hl


def strany(html):
    strana = html.find_all("td", {"class": "overflow_name"})

    strana_soupis = []
    for a in strana:
        text = a.get_text(strip=True)
        strana_soupis.append(text)

    return(", ".join(strana_soupis))


def hlasy_stran(html):
    strana_hlasy_t1 = html.find_all(
        "td", {"class": "cislo", "headers": "t1sa2 t1sb3"})
    strana_hlasy_t2 = html.find_all(
        "td", {"class": "cislo", "headers": "t2sa2 t2sb3"})
    strana_hlasy_celkem = strana_hlasy_t1 + strana_hlasy_t2
    hlasy_soupis = []
    
    for a in strana_hlasy_celkem:
        cislo = a.get_text(strip=True)
        hlasy_soupis.append(cislo)
    
    return (", ".join(hlasy_soupis)) 


def zapis_hlavicky_csv(nazev_csv, strany_soupis):
    with open(nazev_csv, mode="w", encoding="utf-8") as csv_soubor:
        zapisovac = csv.writer(csv_soubor, dialect="excel-tab")
        zapisovac.writerow(("Číslo obce", "Obec", "Voliči", "Vydané obálky", "Platné hlasy", strany_soupis))
        

def zapis_dat_csv(nazev_csv, cislo_obce, obec, volici, obalky, hlasy, hlasy_stran):
    with open(nazev_csv, mode="a", encoding="utf-8") as csv_soubor:
        zapisovac = csv.writer(csv_soubor, dialect="excel-tab")
        zapisovac.writerow((cislo_obce, obec, volici, obalky, hlasy, hlasy_stran))


def vypis_knihoven():
    with open("requirements.txt", "w", encoding = "utf-8") as r:
        subprocess.run(["pip", "freeze"], stdout =r, text=True )


def main():

    url = sys.argv[1]
    # spustíme python main.py "url adresa" "nazev souboru.csv"
    #"https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
    if len(sys.argv) != 3:
        print("Pro spuštění chybí argument url nebo název souboru.")
        sys.exit()
    elif "https://www.volby.cz/pls" not in sys.argv[1]:
        if ".csv" in sys.argv[1]:
            print("Zadali jste špatné pořadí argumentů.")
            sys.exit()
        else:
            print("Zadali jste špatný odkaz.")
            sys.exit()
    elif ".csv" not in sys.argv[2]:
            print("Název musí končit příponou .csv.")
    else:
        #vypis_knihoven()

        finalni_csv = sys.argv[2]
        parsovane_html = parsovani_html(url)

        cisla_vsech_obci = parsovani_cisel_obci(parsovane_html)
        
        obce = nazvy_obci(parsovane_html)

        print("Stahuji data ze zadané URL.")
        x = 0
        while x < len(cisla_vsech_obci):

            url_dane_obce = ziskani_url2(url, cisla_vsech_obci,x)
        
            parsovane_html2 = parsovani_html2(url_dane_obce)

            pocet_volicu = volici(parsovane_html2)

            pocet_obalek = obalky(parsovane_html2)

            platne_hl = platne_hlasy(parsovane_html2)

            hl_stran = hlasy_stran(parsovane_html2)

            strany_soupis = strany(parsovane_html2)

            if x == 0:
                zapis_hlavicky_csv(finalni_csv, strany_soupis)
                print(f"Ukládám data do souboru {finalni_csv}.")

            #zapis_dat_csv(
                #finalni_csv, cisla_vsech_obci[x], obce[x], pocet_volicu, pocet_obalek, platne_hl, hl_stran)

            x += 1

        else: print("Hotovo, ukončuji program.")
        print(obce)

        #print(cisla_vsech_obci[0])
        print(obce)
        #print(pocet_volicu)
        #print(pocet_obalek)
        #print(platne_hl)
        #print(strany_soupis)
        #print(hl_stran)


if __name__ == "__main__":
    main()