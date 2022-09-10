movie = input("Tytul filmu: ")

grade1 = int(input("Ocena filmu w skali 1-10: "))
grade2 = int(input("Ocena muzyki filomwej w skali 1-10: "))
grade3 = int(input("Ocena gry aktorskiej w skali 1-10: "))

print("Film pt. " + movie)
grade_avg = (grade1 + grade2 + grade3)/ 3
print("oceniasz na ", round(grade_avg, 2))

if grade_avg > 7:
    print('Bardzo dobry film')
elif grade_avg >= 5:
    print('Przeciętny')
else:
    print('Słaby')

"""
Dodaj 3 nowe oceny i wylicz srednia z ocen
"""