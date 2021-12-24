#Oppgave 4: Billettpris

#Kommentar: Forst lager jeg en prosedyre og kaller den for enprosedyre. Jeg setter inn
#en variabel i prosedyren jeg kaller for alder. Det er en input hvor bruker
#skal skrive inn alderen sin. Teksten blir gjort om til tall, takket vaere
#int. Hvis alder er lik eller under 17 blir barnebillettprisen 30, og dette blir
#printet. Hvis alderen er over 17 eller mindre enn 63, blir voksenbillettprisen
#50 printet. Hvis alderen er lik eller over 63 blir pensjonsbillettprisen 35 printet. 
#Prosedyren blir kalt på 4 ganger. Når programmet starter hopper den først
#til prosedyrekallet, kjører prosedyren under def. Når den har kjørt prosedyren
#oppdager den det samme prosedyrekallet og kjører prosedyren igjen. Dette skjer
#to ganger til.

def enprosedyre():
    alder= (int(input("Skriv inn alderen din: ")))
    billettpris=0
    if alder <= 17:
        billettpris= 30
        print("Din barnebillett koster", billettpris, "kr.")
    elif alder > 17:
        billettpris=50
        print("Din voksenbillett koster", billettpris, "kr.")
    elif alder >= 63:
        billettpris= 35
        print("Din pensjonistbillett koster", billettpris, "kr.")

enprosedyre()
enprosedyre()
enprosedyre()
enprosedyre()

#6.
#Det som er feil er at hvis man  kjører elif alder > 17:(linje 20), så vil den stoppe på den linjen hvis bruker skriver er lik eller over 63 aar. Dermed vil voksenbillett
#bli printet, ikke pensjonistbillett. Derfor maa man skrive elif alder > 17 and alder < 63: for at programmet skal hoppe videre til pensjonistbillett hvis bruker
#taster inn pensjonistalder. Oppgaven hadde blitt riktig hvis denne hadde blitt skrevet på denne maaten:

def enprosedyre():
    alder= (int(input("Skriv inn alderen din: ")))
    billettpris=0
    if alder <= 17:
        billettpris= 30
        print("Din barnebillett koster", billettpris, "kr.")
    elif alder > 17 and alder < 63:
        billettpris=50
        print("Din voksenbillett koster", billettpris, "kr.")
    elif alder >= 63:
        billettpris= 35
        print("Din pensjonistbillett koster", billettpris, "kr.")

enprosedyre()
enprosedyre()
enprosedyre()
enprosedyre()

