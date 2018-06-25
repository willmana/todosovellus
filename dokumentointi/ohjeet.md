## Asennusohjeet

* Lataa projekti itsellesi
```
https://github.com/willmana/todosovellus
```
* Luo Herokussa osoite
```
heroku create oma-osoite-sovellukselle
```
* Lisää yhteys Herokuun ja gittiin
```
git remote add heroku https://git.heroku.com/oma-osoite-sovellukselle.git
```
* Pushaa projekti Herokuun
```
git add .
git commit -m "Eka commit"
git push heroku master
```
* Luo ympäristömuuttuja Herokuun
```
heroku config:set HEROKU=1
```
* Lisää tietokanta käytettäväksi Herokuun
```
heroku addons:add heroku-postgresql:hobby-dev
```
* Käynnistä tietokanta
```
heroku pg:psql
```
* Lisää tietokantaan käyttäjä (vapaaehtoinen)
```
INSERT INTO account (name, username, password) VALUES ('Käyttäjä', 'Uusi', 'Kayttis');
```
* Hyppää sovelluksen käyttöön!

## Käyttöohjeet (löytyvät myös periaatteessa sovelluksen etusivulta)

* Mene sivulle [ToDo-sovellus](https://tsoha-python-todosovellus.herokuapp.com/), jos olet vanhempi käyttäjä voit kirjautua tunnuksillasi sovellukseen painamalla "Kirjaudu" kohtaa. Jos olet uusi käyttäjä, rekisteröidy sovellukseen painamalla "Rekisteröidy" ja kirjaudu sen jälkeen sovellukseen sisälle.

* Kun olet sisällä, ennen kuin alat tekemään itsellesi askeita, luo kategorioita joihin tahdot luokitella askareet. Painamalla "Lisää kategoria" pääset lisäämään itsellesi kategorioita jotka ovat katsottavissa ja poistettavissa "Listaa kategoriat" napin takana.

* Kun olet luonu itsellesi kategorian tai pari, voit alkaa tekemään itsellesi tehtäviä "Lisää tehtävä" napin kohdalta. Muista valita kategoria tehtävällesi. Tehtäviä voi katsella, poistaa ja merkitä tehdyksi menemällä "Listaa tehtävät" osioon.
