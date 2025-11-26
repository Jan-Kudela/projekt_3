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
pip install <název_knihovny>
```
<h2>Spuštění programu</h2>
<p>Program lze spustit skrze terminál nebo příkazový řádek, nutností je zadat dva systémové argumenty:</p>
<p>1. argument: URL adresa vybraného územního celku</p>

```
např.: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2105
```
<p>2. argument: název souboru, do kterého se výsledky uloží. Soubor musí být ve formátu CSV a název souboru musí tuto příponu také obsahovat.</p>

```
např.: vysledky_kutna_hora.csv
```




