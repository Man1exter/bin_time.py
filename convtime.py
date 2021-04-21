import time

print("[1] Zamiana jednostek..")
print("[2] Dokladny czas lokalny..")
print("[3] Historia o time.sleep")
print(" ")
print(" ")

wybor = int(input("Pozycja z menu =====> "))

def binsys():
  print("[1] Zamiana z liczby binarnej na inne.... ===> (5,12,15,23543) <===")
  print("[2] Z innych na binarna... ===> (1010110,101011000) <=== ")
  print(" ")
  print(" ")

  wybor2 = int(input("Pozycja z menu =====> "))

  if wybor2 == 1:
   x = int(input("Podaj liczbe ===> "))

   print("hex => ",hex(x))
   print("oct => ",oct(x))
   print("bin => ",bin(x))

  elif wybor2 == 2:
   y = input("Podaj liczbe binarna ===> ")

   print("na system dwojkowy(2) ==>",int(y,2))
   print("na system osemkowy(8) ==>",int(y,8))
   print("na system dziesietny(10) ==>",int(y,10))
   print("na system szesnastkowy(16) ==>",int(y,16))
  
def timesys():
      
        print(" ")
        print(" ")
        print("Aktualna data....")
        ctime = time.localtime()
        print(ctime.tm_year,ctime.tm_mon,ctime.tm_isdst)
        print(ctime.tm_hour,ctime.tm_min,ctime.tm_sec,sep=":")
        print(ctime.tm_hour,ctime.tm_min,ctime.tm_sec,sep="-")
        print(ctime.tm_hour,ctime.tm_min,ctime.tm_sec,sep="=")

def storyLife():
      
      print(" ")
      print(" ")
      print("Krotka historia o spaniu z time (:)")
      print(" ")
      print("Ide spac...")
      time.sleep(2) # pod x ile sekund..
      print("Minelo 2 sekundy od kiedy spie..")
      time.sleep(3)
      print("dzieki opcji time.sleep(x) <=== moge trzymac w czasie print jako w  konsoli..")
   

if wybor == 1:
  binsys()
elif wybor == 2:
  timesys()
elif wybor == 3:
  storyLife()
else:
  print("nie wiem co chcesz zrobic..")

