# Oppgave 6
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)  # 200 punkter i intervallet
y = -x**2 - 5  # Funksjonen

plt.plot(x, y)  # Lager plott

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) = -x**2 - 5")
plt.grid(True)

plt.show()  # Viser plottet


