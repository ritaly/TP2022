# Napisz funkcję, która pyta użytkownika o pary film + ocena. Zapamiętaj te dane w dowolny sposób.
# Zapytaj użytkownika o numer filmu i wyświetl film wraz z oceną.
# Obsłuż błąd użytkownika - co jeśli użytkownik zapyta o numer w bazie, który nie istnieje?

movies_grades_list = []

def get_movies(number):
    for i in range(number):
        movie = input("Title? ->")
        grade = input("Grade? ->")
        movies_grades_list.append([movie, grade])

def show_movie_by_id(id):
    title, grade = movies_grades_list[id]
    print(f"Movie {title}, is rated {grade}")

# -------------------------------
# wez liczbe filmow od użytkownika
get_movies(3)
print(movies_grades_list)

id_not_found = True
while id_not_found:
    user_movie_index = int(input("Which film you want check? ")) - 1 # bo użytkownik podaje od 1

    if user_movie_index >= len(movies_grades_list):
        print("Nie ma takiego filmu, spróbuj jeszcze raz")
    else:
        print("Tak mamy ten film! Już Ci pokazuję")
        id_not_found = False

show_movie_by_id(user_movie_index)