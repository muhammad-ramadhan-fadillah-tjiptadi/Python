# hypotenuse.py
import math

# Minta input sisi a dan b
a = float(input("Masukkan panjang sisi a: "))
b = float(input("Masukkan panjang sisi b: "))

# Hitung hipotenusa
c = math.sqrt(a**2 + b**2)

# Tampilkan hasil
print(f"Panjang hipotenusa: {c:.2f}")
