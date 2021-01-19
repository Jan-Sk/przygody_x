#!/bin/env python3
from plansze import *
from dialogi import *
from przedmioty import *     

def pokaz_przedmioty(plecak_bohatera):
    for przedmiot in range(len(plecak_bohatera)):
        nazwa_przedmiotu = plecak_bohatera[przedmiot]
        if nazwa_przedmiotu in przedmioty["bron"]:
            print(f"nazwa przedmiotu: {nazwa_przedmiotu}")
            print(f"    typ: {przedmioty['bron'][nazwa_przedmiotu]['typ']}")
            print(f"    atak: {przedmioty['bron'][nazwa_przedmiotu]['atak']}")
            print(f"    obrona: {przedmioty['bron'][nazwa_przedmiotu]['obrona']}")
            print("\n")
        if nazwa_przedmiotu in przedmioty["artefakty"]:
            print(f"nazwa przedmiotu: {nazwa_przedmiotu}")
            print(f"    opis: {przedmioty['artefakty'][nazwa_przedmiotu]['opis']}")
            print("\n")
        else:
            print("")


plecak_bohatera = [ "zwykly_miecz", "zwykly_lok" ]
zycie = ["=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "="]
mana = ["=", "=", "=", "=", "=", "=", "=", "=", "="]



def plansza():
    print("zycie:", end = "")
    for pasek_zycia in range(len(zycie)):
        print(zycie[pasek_zycia], end = "")

    print("     mana:", end = "")
    for pasek_many in range(len(mana)):
        print(mana[pasek_many], end = "")

    for i in range(len(mapa_1)):
        print("")
        for j in range(len(mapa_1[0])):
            print(mapa_1[i][j], end="")
    print("\n")


#ta funkcja odpowiada za czynnosci ktore sie peda dzialy podczcas wykonywania ruchow postaci
def walidacja_ruchu(x, y, mapa_1, zycie):
    if mapa_1[x][y] == " ":
        return "dozwolony"
        
    elif x == 1 and y == 3:
        mapa_1 = dialog_1(mapa_1, plecak_bohatera)
        return "dialog"
    elif x == 10 and y == 15:
        dialog_2(plecak_bohatera)
        return "dialog"
    elif x == 2 and y == 2:
        print("nie podchodz do mnie!")
        zycie = zycie[:-2]
        return "dialog"  

    elif x == 26 and y == 3:
        plecak_bohatera.append("ksiega_czarow")
        return "dozwolony"
    elif x == 3 and y == 1:
        plecak_bohatera.append("zardzewialy_klucz")
        return "dozwolony"
    else:
        print("ruch niedozwolony")
        return "niedozwolony"

def dodaj_zawartosc_mapy(mapa_1):
    mapa_1[1][3] = "N"
    mapa_1[10][15] = "N"
    mapa_1[2][2] = "N"
    mapa_1[3][1] = "P"
    mapa_1[26][3] = "P"
    return mapa_1


#main

mapa_1 = dodaj_zawartosc_mapy(mapa_1)

x = 1
y = 1
mapa_1[x][y] = "X"
plansza()
while True:

    ruch = input()
    if ruch == "w":
        walidacja = walidacja_ruchu(x-1, y, mapa_1, zycie)
        if walidacja == "dozwolony":
            mapa_1[x][y] = " "
            x = x - 1
            mapa_1[x][y] = "X"

    elif ruch == "s":
        walidacja = walidacja_ruchu(x+1, y, mapa_1, zycie)
        if walidacja == "dozwolony":
            mapa_1[x][y] = " "
            x = x + 1
            mapa_1[x][y] = "X"

    elif ruch == "a":
        walidacja = walidacja_ruchu(x, y-1, mapa_1, zycie)
        if walidacja == "dozwolony":
            mapa_1[x][y] = " "
            y = y - 1
            mapa_1[x][y] = "X"

    elif ruch == "d":
        walidacja = walidacja_ruchu(x, y+1, mapa_1, zycie)
        if walidacja == "dozwolony":
            mapa_1[x][y] = " "
            y = y + 1
            mapa_1[x][y] = "X"
    elif ruch == "i":
        pokaz_przedmioty(plecak_bohatera)

    else:
        print("poruszaj sie uzywajc klawiszy w s a d")
    plansza()
