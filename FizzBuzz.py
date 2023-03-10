#Fizz buzz challenge
for i in range(1, 101):
    fizz = i % 3 == 0
    buzz = i % 5 == 0
    if fizz and buzz:
        print("FizzBuzz")
    elif fizz:
        print("Fizz")
    elif buzz:
        print("Buzz")
    else:
        print(i)