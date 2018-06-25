# Käyttötapaukset

## Jos et ole kirjautunut:

* Käyttäjä voi rekisteröityä
* Käyttäjä voi kirjautua

## Kirjautunut käyttäjä voi:

* Lisätä uuden kategorian
* Listata kaikki järjestelmässä olevat kategoriat
* Poistaa kategorioita järjestelmästä
* Lisätä uusia tehtäviä
* Listata kaikki tehtävät
* Poistaa tehtäviä
* Muokata tehtäviä
* Kirjautua ulos järjestelmästä

## Esimerkkitapauksia

* Olkoon kyseessä opiskelija joka tahtoo merkata omat kurssin palautukset, kotona tehtävät hommat ja vapaa-ajalla suoritettavat askareet samalle listalle ja seurata niitä yhdessä paikassa. Kyseinen henkilö voi käyttää tällöin hyödyksi sovellusta ja seurata samalla kaikkia näitä asioita melko yksinkertaisesti ja tehokkaasti.

* Olkoon kyseessä vaikka perheen äiti. Sovelluksen avulla hän voi merkata kaikki lastensa neuvola ajat, ruokatoiveet lähipäiville ja harrastukset samaan paikkaan mihin merkitsee vaikka omat työasiansa. Sovellus voi toimia tällöin myös koko perheen käytössä ja kaikki voivat lisätä sinne omia tehtäviä tehtäväksi.

## Käytetty SQL-kysely

Kyseistä kyselyä käytetään hyödyksi kun halutaan listata kaikki kategoriaan sisältyvät tehtävät.

```
@staticmethod
    def listaa_tehtavat(id):
        stmt = text('SELECT tehtava.name FROM task_category, tehtava, kategoria'
        ' WHERE task_category.kategoria_id = ' + str(id) +
        ' AND task_category.kategoria_id = kategoria.id'
        ' AND task_category.tehtava_id = tehtava.id')
´´´
