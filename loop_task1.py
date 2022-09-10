num = int(input("Podaj liczbe filmów -> "))

movie_grade_list = []

for _ in range(num):
    movie = input("Tytul filmu: ")
    grade = input("Ocena filmu w skali 1-10: ")
    movie_grade_list.append([movie, grade])

print(movie_grade_list)

# for f in movie_grade_list:
#     print(f)
#     print("Film pt. " + f[0])
#     print("oceniasz na ", f[1])

while movie_grade_list != []:
    movie, grade = movie_grade_list.pop()
    print("Film pt. " + movie)
    print("oceniasz na ", grade)
