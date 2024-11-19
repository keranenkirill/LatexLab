# LatexLab - Ohjelmistotuotannon miniprojekti

[![GHA workflow badge](https://github.com/keranenkirill/LatexLab/workflows/CI/badge.svg)](https://github.com/keranenkirill/LatexLab/actions)

## Järjestelmän kuvaus

Tämän sovelluksen avulla käyttäjä voi lisätä lähdeviitteitä järjestelmään helppokäyttöisen käyttöliittymän kautta. Järjestelmä generoi näistä viitteistä automaattisesti BibTeX-tiedoston, jonka voi helposti liittää LaTeX-dokumenttiin. Sovellus mahdollistaa viitteiden tehokkaan hallinnan, suodatuksen ja organisoinnin, koska LaTeXissa viitteiden hallinta voi olla monimutkaista ja aikaa vievää. Keskittymällä gradun kannalta olennaisiin viitekenttiin sovellus tekee viitteiden hallinnasta käyttäjäystävällisempää ja vähentää manuaalista työtä.


## Dokumentit
* [Manuaali](docs/manuaali.md)
* [Valmiin määritelmä](docs/definitionOfDone.md)
* [Product Backlog](https://docs.google.com/spreadsheets/d/1z1sriGN7_VkhWK3ftrvxO8W_lWaIzaeMN91lBrkc4Ag/edit?gid=1#gid=1)

## Tulevia toimintoja
- **Viitteiden lisääminen:** Mahdollisuus lisätä viitteitä käyttäjäystävällisen lomakkeen kautta.
- **Viitteiden listaus:** Viitteet voidaan listata selkeästi ja luettavassa muodossa.
- **Viitte tiedoston generoiminen:** Viitteestä voi generoida LaTeX-dokumenttiin yhteensopiva BibTeX-tyyppinen tiedosto.
- **Viitteiden suodattaminen:** viitteen tyypin, kirjoittajanm,vuoden tai julkaisun mukaan. 

## Teknologiat
- poetry
- Flask
- PostgreSQL
- Python
- Robot Framework

## Asennusohje

Kloonaa repositorio
```bash
git clone git@github.com:keranenkirill/LatexLab.git
```
Riippuvuuksien asentaminen
```bash
poetry install
```
Siirry Poetry-virtuaaliympäristöön
```bash
poetry shell
```
Ennen ensimmäistä käynnistystä luo tietokantataulu 
```bash
python src/db_helper.py
```
Käynnistä sovellus komennolla
```bash
python src/index.py
```
Mene selaimella osoitteeseen
```bash
localhost:5001
```
Lopeta sovellus painamalla
```bash
ctrl + c
```
