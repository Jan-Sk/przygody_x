#!/bin/env python3
import datetime

def ile_dni_zyjesz(rok, miesaic, dzien, dzisiaj):
    dzien_urodzin = datetime.datetime(rok, miesiac, dzien)
    ilosc_dni = dzisiaj - dzien_urodzin
    return ilosc_dni

#main
dzisiaj = datetime.datetime.now()

while True:
    rok = input("podaj rok swoich urodzin: ")
    if rok.isnumeric() is True:
        break
    print("rok musi byc podany w postaci liczby")

miesiac = input("podaj miesiac swoich urodzin: ")
dzien = input("podaj dzien swoich urodzin: ")
ilosc_dni = ile_dni_zyjesz(rok, miesiac, dzien, dzisiaj)

print(f"na tym swiecie zyjesz juz {ilosc_dni}")