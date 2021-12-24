#Oppgave 2: Ordbok

#1.
#Kommentar: Forst lager jeg en ordbok og plasser varene og hvor mye hver vare koster,
#deretter printer jeg ordboken. 
varerogpris= {"melk": 14.90, "brød": 24.90, "yoghurt": 12.90, "pizza": 39.90}
print(varerogpris)

#Kommentar: Jeg spor brukeren hvilken vare han eller hun vil legge inn i ordboken, spor hva varen skal koste på neste linje,
#og lagrer dem i hver sin variabel. Dette gjor jeg igjen. Nar jeg spor om pris bruker jeg float, tilfelle bruker skriver
#inn et desimaltall. Deretter legger jeg varene og prisene inn i ordboken og printer den. 
#2.
vare1= input("Hvilken vare vil du legge inn i ordboken?")
pris1= (float(input("Hva skal varen koste?")))
vare2= input("Hvilken vare vil du legge inn i ordboken?")
pris2= (float(input("Hva skal varen koste?")))

varerogpris[vare1]=pris1
varerogpris[vare2]=pris2
print(varerogpris)
