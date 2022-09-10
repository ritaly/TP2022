"""
Sprawdź czy pobrany tekst ze strony zawiera liczbę "13"
Zapytaj użytkownika o dowolny ciąg znaków.
Sprawdź czy tekst ze strony zawiera też ciąg zadany przez użytkownika
"""
import requests
req = requests.get("http://numbersapi.com/random/year") # odpytujemy API

txt = req.text
print(txt)

if '13' in txt:
    print('Jest 13 w tekście')

substr = input('Podaj tekst do sprawdzenia: ')

if substr in txt:
    print(f"--> {substr} występuje w tekście")
else:
    print(f"--> {substr} nie występuje w tekście")