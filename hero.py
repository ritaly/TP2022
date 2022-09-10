heros = []
num = int(input("Ilu bohaterów chcesz dodać ... -> "))

for _ in range(num):
    boh = input("podaj bohatera-> ")
    heros.append(boh)

if 'Killer' in heros:
    print('Found the killer!')
else:
    print('No killer')


# found_killer = False
# for h in heros:
#     if h == "Killer":
#         print("Found the killer!")
#         found_killer = True
#
# if not found_killer:
#     print('No killer')

