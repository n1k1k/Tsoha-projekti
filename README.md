## Keskustelufoorumisovellus

Sovelluksessa on viestiketjuja, jotka muodostuvat alkuperäisestä viestistä ja kommenteista. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

Sovelluksen ominaisuuksia:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä voi muokata tilinsä tietoja.
- Käyttäjä voi seurata muita käyttäjiä.
- Käyttäjä näkee sovelluksen etusivulla listan viestiketjuista niin, että uusin viestiketju on ensimmäisenä.
- Käyttäjä voi suodattaa viestiketjuja niin, että hän näkee vain seuraamiensa käyttäjien luomat viestiketjut.
- Käyttäjä voi luoda uuden viestiketjun antamalla sille otsikon ja viestin sisällön. 
- Käyttäjä voi kirjoittaa uuden kommentin olemassa olevaan viestiketjuun.
- Käyttäjä voi poistaa itse tekemänsä viestiketjun ja muokata sen sisältöä.
- Käyttäjä voi poistaa itse tekemänsä kommentin.
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
- Ylläpitäjä voi poistaa käyttäjiä.
- Ylläpitäjä voi poistaa viestiketjuja.
- Ylläpitäjä voi hakea käyttäjiä käyttäjänimellä tai id-numerolla.
- Ylläpitäjä voi hakea viestiketjuja ketjun id-numerolla.

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
Tietokantaan voi testaamista varten lisätä sisältöä komennolla:<br />
  `$ psql < seed.sql`<br />
Tällöin sovelluksessa on valmiiksi yksi ylläpitäjä, jonka tunnus on `god_of_lightning@fake-email.com` ja salasana `test` ja tavallinen käyttäjä , jonka tunnus on `god_of_sea@fake-email.com` ja salasana `test`.

Nyt voit käynnistää sovelluksen komennolla<br />
  `$ flask run`
