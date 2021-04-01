import time

print("[1] Zamiana jednostek..")
print("[2] Dokladny czas lokalny..")
print(" ")
print(" ")

wybor = int(input("Pozycja z menu =====> "))

def binsys():
  print("[1] Zamiana z liczby binarnej na inne....")
  print("[2] Z innych na binarna...")
  print(" ")
  print(" ")

  wybor2 = int(input("Pozycja z menu =====> "))

  if wybor2 == 1:
   x = int(input("Podaj liczbe binarna ===> "))

   print("hex => ",hex(x))
   print("oct => ",oct(x))
   print("bin => ",bin(x))

  elif wybor2 == 2:
   y = input("Podaj liczbe binarna ===> ")

   print("na dwojkowy ==>",int(y,2))
   print("na osemkowy ==>",int(y,8))
   print("na szesnastkowy ==>",int(y,16))
  
def timesys():
        print(" ")
        print(" ")
        print("Aktualna data....")
        ctime = time.localtime()
        print(ctime.tm_year,ctime.tm_mon,ctime.tm_isdst)
        print(ctime.tm_hour,ctime.tm_min,ctime.tm_sec,sep=":")
   

if wybor == 1:
  binsys()
elif wybor == 2:
  timesys()
else:
  print("nie wiem co chcesz zrobic..")

