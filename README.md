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

# Versio 1.1
Palautus 3

Tietokantasovelluksen uusin versio on testattavissa [Herokussa](https://tsoha-messageboard.herokuapp.com/)

Tähän versioon tehdyt lisäykset ja parannukset:
- Ulkoasu on lisätty.
- Aiheiden lisääminen onnistuu nyt vain ylläpitäjiltä.
- Ylläpitäjä voi luoda alueen jonne pääsee vain ylläpitäjät.
- Hakutoiminto on lisätty.
- Aiheet ovat yhdistetty viesteihin. Aihetta painamalla pääsee lukemaan siihen aiheeseen kirjotetut viestit.

Tietoturvan kannalta tehdyt parannukset:
- Ylläpitäjän rooli on otettu käyttöön esimerkiksi aiheiden lisäämisessä.
- Kirjautumisen tarkistuksia on lisätty, ettei aiheisiin tai viesteihin pääse käsiksi ilman kirjautumista.

Huomioita:
- Uloskirjaumisen yhteydessä käyttäjä jää "roikkumaan". Jos samalla koneella kirjautuu uusi käyttäjä niin hänen kirjoittamansa viestit tulevat tuplana tietokantaan.
- Ylläpitäjille tarkoitetulle keskustelualueelle pääsee kiertämään sisään muokkaamassa selaimen osoitetta kirjoittaessa uutta viestiä.

Parannettavaa seuraavaan versioon
- Viesteihin pitäisi vielä saada seuraava taso. Nykyiset viestit olisivat viestiketjuja joiden sisään pääsee vielä lisäämään erikseen viestin.
- Ulkoasun parantelua ja tekstien parempaa sommittelua.
- Virheiden korjausta.

# Vesio 1.2
Viimeinen palautus

Tietokantasovelluksen uusin versio on testattavissa [Herokussa](https://tsoha-messageboard.herokuapp.com/)

Tähän versioon tehdyt lisäykset ja parannukset:
- Ulkoasu on viimeistelty. Ohje tekstit on käyty lävitse ja mietitty mahdollisimman hyödyllisiksi käyttäjälle. Ulkoasu on yhtenäistetty kaikille sivuille samaksi.
- Viesteihin on lisätty "uusi ulottuvuus". Aikaisemmin käyttäjä kirjoitti viestin suoraan aiheeseen. Nyt on lisätty rakenne jossa on aihe, viestiketju sekä lopuksi vasta viestit.
- Hakutoiminto on viimeistelty ja sitä on monipuolistettu esimerkiksi suorilla linkeillä joilla voi siirtyä esimerkiksi aiheeseen. 
- Hakua on paranneltu ymmärtämään syötteitä vaikka viesti sisältäisi isoja kirjaimia.
- Viestien muokkaustoiminta on lisätty. Käyttäjä pääsee kätevästi näkemään omat viestinsä koosteena ja muokkaamaan niitä halutessaan.
- Viesteistä voi nyt tykätä ja ne kerryttävät viestien kirjoittajalle tykkäyksiä. Tykkäysten määrä on nähtävissä koosteena sille varatulla sivulla.
- Taulujen määrää on lisätty ominaisuuksien kasvaessa.
- Tietokantoja käsitellään monipuolisemmin.
- Syötteiden validointia on parannettu. Tyhjiä kenttiä ei pitäisi pystyä lähettämään. Tykkäykset onnistuvat vain toisten viesteistä.

Tietoturvan kannalta tehdyt parannukset:
- CSRF-haavoittuvuus on paikattu.

Huomioita:
- Ylläpitäjän rooli ei aivan asetu kohdilleen. Piilotettuja ylläpitäjien kanavia ei alkuperäisen suunnitelman mukaisesti vielä löydy.
- Satunnaisesti, mutta harvoin edellisiin sivuihin palaamiseen tarkoitetut painikkeet johdattavat virheelliselle sivulle.
- Alkuperäisen suunnitelman mukaisia aikaleimoja esimerkiksi muokatuista viesteistä puuttuu.
- Alkuperäisen suunnitelman vastaisesti viestien poistaminen ei toimi.
- Vastapainoksi alkuperäisen suunnitelman "mahdollisia ominaisuuksia" on otettu käyttöön. 
- Lisäksi jo toiminnassa olevista ominaisuuksista on yritetty tehdä mahdollisimman laadukkaita ja monipuolisia.

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

