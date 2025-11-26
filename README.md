<h1><strong>Popis projektu</strong></h1>
<h2>Elections Scraper</h2>
<p> Třetí projekt v rámci kurzu Tester s Pythonem u Engeto.cz</p>
<p>Tento program slouží k extrahování výsledků parlamentních voleb z roku 2017 
z webových stránek Volby.cz.  
Odkaz pro konkrétní územní celky naleznete 
<a href="https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ">zde</a>.
</p>

<h2><strong>Instalace virtuálního prostředí</strong></h2>
<p>Před instalací knihoven doproučuji použít nové virtuální prostředí, které vytvoříte následovně:</p>
<p>Windows:</p>

```
python -m venv <název_vrituálního_prostředí>
```
<p>Aktivace virtuálního prostředí:</p>

```
<název_vrituálního_prostředí>\Scripts\Activate.ps1
```
<h2><strong>Instalace knihoven</strong></h2>

<p>Soupis použitých knihoven třetích stran a jejich verze nalezente v souboru requirements.txt. </p>
<p>Instalaci provedete příkazem:</p>

```
pip install -r requirements.txt
```
<h2>Spuštění programu</h2>
<p>Program lze spustit skrze terminál nebo příkazový řádek, nutností je zadat dva argumenty. Pokud bude zadán špatný počet argumentů nebo budou zadány ve špatném pořadí, bude uživatel upozorněn.</p>

<h2>Ukázka projektu</h2>
Výsledky hlasování pro okres Opava:

<p>1. argument: URL adresa vybraného okresu:</p>

```
https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8105
```
<p>2. argument: název souboru, do kterého se výsledky uloží. Soubor musí být ve formátu CSV a název souboru musí tuto příponu také obsahovat:</p>

```
vysledky_opava.csv
```
<p>Celý příkaz pro spuštění:</p>

```
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8105" "vysledky_opava.csv"
```
<p>Průběh programu:</p>

```
<p>Stahuji data ze zadané URL.</p>
<p>Ukládám data do souboru vysledky_opava.csv</p>
<p>Ukončuji program</p>
```

<p>Částečný výstup:</p>


