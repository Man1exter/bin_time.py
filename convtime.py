
print("[1] Zamiana jednostek..")
print("[2] Dokladny czas lokalny..")

wybor = int(input("Pozycja z menu =====> "))

def binsys():
  print("Zamiana z liczby binarnej na inne....")
  x = int(input("Podaj liczbe binarna ===> "))

  print("hex => ",hex(x))
  print("oct => ",oct(x))
  print("bin => ",bin(x))

if wybor == 1:
  binsys()
elif wybor == 2:
  print("ok")

