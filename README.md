# Keskustelusovellus
TKT20011 Harjoitustyö

Tässä sovelluksessa käyttäjät voivat osallistua keskusteluihin itseänsä kiinnostavista aiheista. Aihealueet ovat valmiiksi luotuja ylläpitäjien toimesta.
Alueilla on erikseen viestiketjuja, joita käyttäjät pystyvät lisäämään sekä kirjoittamaan niihin uusia viestejä. Sovellukseen rekisteröityneet ovat joko käyttäjiä tai ylläpitäjiä.

# Versio 1.0
Palautus 2

Tietokantasovellus on testattavissa [Herokussa](https://tsoha-messageboard.herokuapp.com/)

Tähän versioon on saatu hyvälle mallille seuraavat ominaisuudet:
- Testikäyttäjä voi luoda tunnuksen ja kirjautua sillä sisään. Sovellus tarkistaa, ettei saman nimistä käyttäjää ole jo rekisteröitynyt palveluun.
- Testikäyttäjä voi luoda uuden aiheen keskustelualueelle.
- Testikäyttäjä voi luoda uuden viestin.
- Sivun käytettävyyttä on yritetty helpottaa lisäämällä käyttäjälle hyödyllisiä toimintoja. Tästä esimerkkinä mahdollisuus palata avustavien tekstien saattelemana linkistä paikkaan johon käyttäjä voisi mahdollisesti haluta siirtyä seuraavaksi.
- Testikäyttäjä saa virheilmoitukset mahdollisista kirjautumiseen liittyvistä virheistä.

Tietoturvan kannalta luodut ominaisuudet:
- Virheilmoitukset ovat tarkoituksella hieman geneerisiä, jottei testaaja saa esimerkiksi vihiä tietokantaan jo luoduista käyttäjistä.
- Kirjautumisen yhteydessä syötetty väärä salasana ohjaa testikäyttäjän virhesivulle. Tällä yritämme vaikeuttaa esimerkiksi useamman salasanan testaamisen nopeasti vilpillisissä tarkoituksissa.

Huomioita:
Tässä muutama ominaisuus jotka näkyvät testaajalle jotta tietokantaan saadaan tuleville versioille tarpeellista tietoa.
- Testikäyttäjä voi valita tunnuksen luomisen yhteydessä haluaako hän olla käyttäjä vai ylläpitäjä. Tämä toiminnallisuus on testissä, jotta myöhemmässä vaiheessa saamme eroteltua käyttäjät ja ylläpitäjät.
- Testikäyttäjä voi valita aihettu luodessaan näkyykö aihe vain ylläpitäjille. Tämä toiminnallisuus on testissä, jotta myöhemmässä vaiheessa saamme tietyt aiheet ja viestit näkymään vain ylläpitäjille.

Parannettavaa seuraavaan versioon
- Kirjoitettujen viestien liittäminen niille tarkoittuihin aiheisiin.
- Sisäänkirjautumisen ominaisuuksien parantaminen.
- Tietyt ominaisuudet ovat vain ylläpitäjien käytössä.
- Ominaisuuksien ja tietokannan taulujen lisääminen.
- Paremman ulkoasun hahmottelu.

# Ominaisuudet:

Sovelluksen ominaisuudet:
- Käyttäjä voi luoda tunnukset palveluun ja kirjautua sisään. Käyttäjä voi valita itselleen nimimerkin, joka näkyy hänen lähettämissään viesteissä.
- Käyttäjä näkee etusivulla ylläpitäjien luomat keskustelualueet ja voi siirtyä haluamalleen keskustelualueelle. 
- Käyttäjä näkee keskustelualueella olemassa olevat viestiketjut. Käyttäjä pystyy lisäämään uuden viestiketjun ja kirjoittamaan siihen uuden viestin. 
- Käyttäjä pystyy myös kirjoittamaan viestejä jo olemassa oleviin ketjuihin.
- Viestiketjun otsikon yhteydessä näkyy myös aika koska se on luotu, sekä koska sinne on kirjoitettu uusi viesti.
- Käyttäjä voi muokata tai poistaa itse lähettämiään viestejä. Muokkauksen tai poistamisen yhteyteen jää merkintä koska viestiä on muokattu tai koska se on poistettu.
- Käyttäjä voi etsiä haluamallaan sanalla viestejä jotka sisältävät kyseisen sanan.
- Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
- Ylläpitäjä voi luoda keskustelualueen joka näkyy vain muille ylläpitäjille.

Mahdollisia ominaisuuksia:
- Käyttäjät voivat antaa toisille käyttäjille "kunniaa". Paljon "kunniaa" omaavaa käyttäjää voidaan pitää luotettavana käyttäjänä.
- Ylläpitäjä voi luoda keskustelualueen joka näkyy vain tietyn verran "kunniaa" saaneille käyttäjälle.
- Ylläpitäjä voi halutessaan nollata käyttäjän "kunniat" esimerkiksi huonon käytöksen takia.
- Ylläpitäjä voi halutessaan antaa käyttäjälle "porttikiellon" tietyksi ajaksi, esimerkiksi huonon käytöksen takia. Porttikiellon aikana käyttäjä ei pääse käyttämään tiliään.

