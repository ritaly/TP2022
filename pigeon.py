from random import randrange

bird = "duck"
while bird != "pigeon":
    print("waiting...")
    num = randrange(0, 101)
    print('number -> ', num)
    if num < 30:
        bird = "pigeon"
print("I'm a pigeon!")
