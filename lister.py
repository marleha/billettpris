#Oppgave 1: Lister

#1.
#Første lager jeg en liste1 og setter inn tre ulike tall. På neste linje tilfører jeg et
#nytt tall i listen. Etterpå printer jeg første element og tredje element i listen.
liste1=[4,2,7]
liste1.append(9)
print(liste1[0], liste1[2])

#2.
#Jeg ber bruker oppgi et navn fire ganger og lagrer dem i hver sin variabel. Deretter
#lager jeg en ny liste, som jeg kaller liste2, og plasserer alle navnene i den
#nye listen.
navn1= input("Oppgi et navn:")
navn2= input("Oppgi et navn:")
navn3= input("Oppgi et navn:")
navn4= input("Oppgi et navn:")
liste2= [navn1, navn2, navn3, navn4]

#3.
#Jeg forteller programmet at hvis navnet mitt er i liste2 så skal den printer
#at bruker husket meg, men hvis navnet mitt ikke er i liste2, skal programmet printe
#Glemte du meg?.
if "Marlene" in liste2:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

#4.
#Jeg lager en ny liste som jeg kaller liste3 og legger inn liste1 og liste2 inn i listen.
#Deretter printer jeg liste3. På neste linje fjerner jeg det siste elementet som er på
#7. plass i liste3, og deretter fjernet det neste siste elementer som er på 6.
#plass. Det er viktig at jeg fjerner det siste elementet først, fordi programmet
#jobber fra linje til linje og hvis jeg starter med 6. plass, vil 7.plass bytte til
#6.plass. Hvis jeg  deretter ber programmet å fjerne 7.plass i listen, er plassen utenfor
#listen. Isåfall må jeg fjerne 6.plass igjen. Til slutt printer jeg liste3.

liste3= liste1 + liste2
print(liste3)
liste3.pop(7)
liste3.pop(6)
print(liste3)
