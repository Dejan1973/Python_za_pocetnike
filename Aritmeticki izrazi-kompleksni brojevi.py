
########## Sabiranje, oduzimanje, mnozenje, deljenje, celobrojno deljenje, stepenovanje, ostatak pri deljenju ######

a = 100
a += 10
print(a)

a = 100
a -= 10
print(a)

a = 100
a *= 10
print(a)

a = 100
a /= 10
print(a)

a = 100
a //= 10
print(a)

a = 100
a **= 10
print(a)

a = 777
a %= 10
print(a)

####### Kvadratni koren #####################

import math ### Standardna Biblioteka "math" redi samo u domenu realnih brojeva

a = 89
b = math.sqrt(a)
print(b)

import cmath  ### "cmath Biblioteka radi u domenu KOMPLEKSNIH, tj. IMAGINARNIH brojeva

a = -89
b = cmath.sqrt(a)
print(b)  ### Rezultat je 9.433981132056603j IMAGINARNI broj kojeg prepoznajemo po slovnoj oznaci "j" na kraju

a = 2
b = 20
c = 2

x1 = (-b + cmath.sqrt (b**2 - 4*a*c))/(2*a)
x2 = (-b - cmath.sqrt (b**2 - 4*a*c))/(2*a)

print(x1)
print(x2)

# # Apsolutna vrednost kompleksnog broja

c = (-71 -0.5j)
c = abs(c)
print(c) # Dobija se netacan rezultat 71.00176054155277

""" Moramo prvo izracunati apsolutnu vrednost realne komponente
    a zatim apsolutnu vrednost imaginarne komponente
    i to smestimo kao jedan kompleksan broj
"""
# Kako mozemo da utvrdimo realnu komponentu kompleksnog broja

c = (-71 -0.5j)
cr = abs(c.real) # Izracunavamo apsolutnu vrednost od realnog dela kompleksnog broja
print(cr)

c = (-71 -0.5j)
ci = abs(c.imag)
print(ci)

# Sada mozemo da stvorimo novi broj sastavljen iz apsolutne vrednosti realnog i imaginarnog broja

ca = (cr +ci*1j)
print(ca)

# Objedinjeno u kracem koraku

ca = (abs(c.real) + abs(c.imag)*1j)
print(ca)

a = (-2 +3j)
b = ( 3 -1j)
c = a + b
print (c)

a = (-2 +3j)
b = ( 3 -1j)
c = a - b
print (c)

a = (-2 +3j)
b = ( 3 -1j)
c = a * b
print (c)

a = (-2 +3j)
b = ( 3 -1j)
c = a / b
print (c)

# Preracunavanje temperature iz celzijusa u farhajd
# Tf = Tc * 1.8 + 32

tC = 24.5
tF = tC * 1.8 +32
print(tF)

# Preracunavanje temperature iz farhajda u celzijusima

tF = 76.1
tC = (tF - 32) / 1.8
tC = round(tC, 1)
print(tC)

# Lmi = Lkm / 1.609345

lkm = 120
lmi = lkm / 1.609345
print(lmi)
