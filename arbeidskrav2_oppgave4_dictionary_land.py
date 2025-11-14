# Oppgave 4

# a) lager dictionary med land: [hovedstad, innbyggere i mill.]
data = {
        "Norge": ["Oslo", 0.634], 
        "England": ["London", 8.982], 
        "Frankrike": ["Paris", 2.161], 
        "Italia": ["Roma", 2.873] 
}

# b) Ber brukeren skrive inn et land
land = input("Skriv inn et land: ")

if land in data:
    hovedstad, innbyggere = data[land]
    print(f"{hovedstad} er hovedstad i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.")
else:
     print("Landet finnes ikke i databasen.")
     
# C) Legger til nytt land
nytt_land = input("SKriv inn et nytt land: ")

hovedstad = input(f"Hva er hovedstaden i {nytt_land}? ")
innbyggere = float(input(f"Hvor mange mill. innbyggere er det i {hovedstad}?"))

data[nytt_land] = [hovedstad, innbyggere]  # Oppdaterer i dictionaryen

print(data)  # Skriver ut resutatet

