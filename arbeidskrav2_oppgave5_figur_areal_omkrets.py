# Oppgave 5
import math

def figur(a,b):
    # Areal av trekanten
    areal_trekant = (a * b) / 2
    
    # Radius til halvsirkelen
    radius = a / 2
    
    # Areal av halvsirkel
    areal_halvsirkel = (math.pi * radius**2) / 2
    
    # Samlet areal
    areal_total = areal_trekant + areal_halvsirkel
    
    # Hypotenus (ytre side)
    hypotenus = math.sqrt(a**2 + b**2)
    
    # Halvsirkelens bue
    omkrets_halvsirkel = math.pi * radius
    
    # Total ytre omkrets
    omkrets_total = a + b + hypotenus + omkrets_halvsirkel
    
    return areal_total, omkrets_total

a = float(input("Skriv inn a: "))
b = float(input("SKriv inn b: "))

areal, omkrets = figur(a,b)

print(f"Arealet er {areal}")
print(f"Den ytre omkretsen er {omkrets}")

    
    