# Oppgave 2
import math  #brukes for å runde opp

antall_elever = int(input("Skriv inn antall elever: "))

pizzaer = antall_elever * 0.25  # 1/4 pizza per elev
pizzaer_rundet_opp = math.ceil(pizzaer)  # runder oppt til nærmeste heltall
print(f"Det må handles inn {pizzaer_rundet_opp} pizzaer til festen.")
