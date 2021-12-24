#Oppgave 5: Egen oppgave

#1 
#Du skal handle på butikken! Lag en handleliste hvor du har melk, ost, sukker og mel. Tenk at du går i butikken. Du finner ost, og
#fjerner den fra handlelisten din. I butikken kommer du på at du har lyst på sjokolade! Du skriver sjokolade på 
#slutten av listen din. Du finner melk og  mel og fjerner disse fra listen. Du kommer på at du trenger tannkrem, sjampoo og vaskemiddel. 
# Det er ikke mer plass å skrive videre på listen og du bestemmer deg for å skrive varene først i listen. Du bestemmer deg for å ikke kjøpe 
#sukker, og bytter ut sukker med frukt. Print deretter listen for å se hvordan listen ser ut og hvilke varer du har igjen. Etterpå printer du
#antall varer du har i listen.

handleliste= ["melk", "ost", "sukker", "mel"]
handleliste.pop(1)
handleliste.append("sjokolade")
handleliste.pop(0)
handleliste.pop(1)
handleliste.insert(0, "tannkrem")
handleliste.insert(0, "sjampoo")
handleliste.insert(0, "vaskemiddel")
handleliste[0]="frukt"
print(handleliste)
print(len(handleliste))

#Kommentar: Forst lagret jeg varene i en liste jeg kalte for handleliste. Deretter fjernet jeg andre element eller varen  i listen ved å skrive inn
#indeks 2. Etterpå la jeg til en vare til i listen. Deretter fjernet jeg forste element og andre element som ligger på indeks 0 og 1. Jeg legger til 
# tre varer etter hverandre foran i handlelisten på indeks 0. Jeg bytter ut sjokolade som ligger på indeks 0 med frukt.Listen printes, og antall
#elementer i listen printes.