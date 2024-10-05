## Keskustelufoorumisovellus

Sovelluksessa on viestiketjuja, jotka muodostuvat alkuperäisestä viestistä ja kommenteista. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

Sovelluksen ominaisuuksia:

:white_check_mark: = Tällä hetkellä toimivat ominaisuudet 

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen :white_check_mark:
- Käyttäjä voi muokata tilinsä tietoja :white_check_mark:
- Käyttäjä voi seurata muita käyttäjiä :white_check_mark:
- Käyttäjä näkee sovelluksen etusivulla listan viestiketjuista :white_check_mark:
- Käyttäjä voi suodattaa viestiketjuja niin että hän näkee vain seuraamiensa käyttäjien luomat viestiketjut :white_check_mark:
- Käyttäjä voi luoda uuden viestiketjun antamalla sille otsikon ja viestin sisällön. :white_check_mark:
- Käyttäjä voi kirjoittaa uuden kommentin olemassa olevaan viestiketjuun :white_check_mark:
- Käyttäjä voi poistaa itse tekemänsä viestiketjun :white_check_mark:
- Käyttäjä voi poistaa itse tekemänsä kommentin :white_check_mark:
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
- Ylläpitäjä voi poistaa käyttäjiä. :white_check_mark: 
- Ylläpitäjä voi poistaa viestiketjuja :white_check_mark:  ja kommentteja.

## Asennus

Kloonaa repositorio ja lue sen juurikansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

  DATABASE_URL=tietokannan-paikallinen-osoite <br />
  SECRET_KEY=salainen-avain <br />

Aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:<br />
  `$ python3 -m venv venv`<br />
  `$ source venv/bin/activate`<br />
  `$ pip install -r ./requirements.txt`

Määritä tietokannan skeema komennolla:<br />
  `$ psql < schema.sql`<br />
Tietokantaan voi testaamista varten lisätä datan komennolla:<br />
  `$ psql < seed.sql`<br />
Tällöin sovelluksessa on valmiiksi yksi ylläpitäjä, jonka tunnus on `god_of_lightning@fake-email.com` ja salasana `test` ja tavallinen käyttäjä , jonka tunnus on `god_of_sea@fake-email.com` ja salasana `test`.

Nyt voit käynnistää sovelluksen komennolla<br />
  `$ flask run`
