## Keskustelufoorumisovellus

Sovelluksessa on viestiketjuja, jotka muodostuvat alkuperäisestä viestistä ja kommenteista. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

Sovelluksen ominaisuuksia:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen etusivulla listan viestiketjuista siten, että uusin ketju näkyy ensimmäisenä.
- Käyttäjä voi luoda uuden viestiketjun antamalla sille otsikon ja viestin sisällön.
- Käyttäjä voi kirjoittaa uuden kommentin olemassa olevaan viestiketjuun.
- Käyttäjä voi poistaa itse tekemänsä viestiketjun tai kommentin.
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
- Ylläpitäjä voi poistaa viestiketjuja ja kommentteja.

## Asennus

Kloonaa repositorio ja lue sen juurikansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

  DATABASE_URL=tietokannan-paikallinen-osoite <br />
  SECRET_KEY=salainen-avain <br />

Aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:<br />
  `$ python3 -m venv venv`<br />
  `$ source venv/bin/activate`<br />
  `$ pip install -r ./requirements.txt`

Määritä tietokannan skeema komennolla:<br />
  `$ psql < schema.sql`

Nyt voit käynnistää sovelluksen komennolla<br />
  `$ flask run`
