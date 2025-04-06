# x = int(input("Unesite ceo broj: "))
# for i in range(x, 0, 1):
#     print(i)

# x = 3
# while x<61:
#     if x%5==0:
#         print(x)
#     x += 1

# x = 1
# suma = 0
# while x<=100:
#     print("Stara vrednost sume iznosi:", suma)
#     print("Trenutni broj:", x)
#     suma = suma+x
#     print("Nova vrednost sume iznosi:", suma)
#     print("---------------")
#     x += 1
# print("Suma:", suma)
###############################################################

# from tkinter import *
#
# def prikaz_teksta():
#     tekst = polje.get()
#     unos_korisnika["text"] = tekst
#
# root = Tk()
# ime_i_prezime = Label(root, text="Dejan Simic")
# ime_i_prezime.grid(row=0, column=0)
#
# unos_korisnika = Label(root, text="")
# unos_korisnika.grid(row=1, column=0)
#
#
# polje = Entry(root)
# polje.grid(row=0, column=1)
#
# dugme = Button(root, text="Prikazi", command=prikaz_teksta)
# dugme.grid(row=1, column=1)
#
# root.mainloop()
##############################################################W

from tkinter import *
root = Tk()

def racun():
    olovke = int(olovkePolje.get())
    sveske = int(sveskePolje.get())

    olovkeCena = 20
    sveskeCena = 30

    novac = olovke * olovkeCena + sveske * sveskeCena
    trosak["text"] = f"Trosak: {str(novac)}rsd"

naslov = Label(root, text="Kupovina za skolu")
naslov.grid(row=0, columnspan=2)

olovkeTekst = Label(root, text="Olovke")
olovkeTekst.grid(row=1, column=0)

sveskeTekst = Label(root, text="Sveske")
sveskeTekst.grid(row=2, column=0)

olovkePolje = Entry(root)
olovkePolje.grid(row=1, column=1)

sveskePolje = Entry(root)
sveskePolje.grid(row=2, column=1)

dugme = Button(root, text="Izracunaj", command=racun)
dugme.grid(row=3, column=0)

trosak = Label(root,text="")
trosak.grid(row=3, column=1)





root.mainloop()


