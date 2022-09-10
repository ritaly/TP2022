def hi(number, name):
    print('Hej!' * number)
    print(name, 'Jak się masz?')

names = ['Ada', 'Julia', 'Ruby']
for n in names:
    len_name = len(n)
    hi(len_name, n)
    print('next')
