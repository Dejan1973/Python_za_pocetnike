################################################
godinaUpisa = 2025
godinaDiplomiranja = godinaUpisa + 4

print(godinaDiplomiranja)
##################################################

godinaUpisa = input("Unesite godinu upisa studenta: ")
godinaUpisa = int(godinaUpisa) #### Pretvaranje teksta u celobrojni tip podatka #######
godinaDiplomiranja = godinaUpisa + 4

print("Godina diplomiranja bi trebalo da bude", godinaDiplomiranja)
###################################################

godinaUpisa = input("Unesite godinu upisa studenta: ")
godinaUpisa = int(godinaUpisa)
godinaDiplomiranja = godinaUpisa + 4
godinaDiplomiranja = str(godinaDiplomiranja) #### Pretvaranje celobrojnog tipa podatka u tekst #######

print("Godina diplomiranja bi trebalo da bude" + godinaDiplomiranja)

####################################################

a = 10
b = 3
c = a + b
print(c)  ########### Sabiranje #################

a = 10
b = 3
c = a - b
print(c)   ########### Oduzimanje #################

a = 10
b = 3
c = a * b ########### Mnozenje #################
print(c)

a = 10
b = 3
c = a / b ############# Deljenje #################
print(c)

a = 10
b = 3
c = a // b
print(c)   ############# Celobrojno deljenje ########

a = 10
b = 3
c = a ** b
print(c)  ########### Stepenovanje ###############

#############################################################

import math

a = 10
b = 3
c = math.sqrt(a)
c = round(c, 4)
print(c)
