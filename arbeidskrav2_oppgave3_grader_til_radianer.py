# Oppgave 3
import numpy as np  # For å bruke pi

v_grad = float(input("Skriv inn gradtallet: "))

v_rad = v_grad * np.pi / 180  # Formel grader → radianer

print(f"{v_grad} grader tilsvarer {v_rad} radianer.")
