x = 25
if x == 28:
    print("Yes you Right")
else:
    print("No you a wrong")
print("=====================")

age = 2

if (age <= 4):
    print("You are baby")
elif (age > 4) and (age < 12):
    print ("You are kids")
elif (age >= 12) and (age < 19):
    print("you are tenager")
else:
    print("You are old")
print("===END===")

all_cars = ["cruasler", "dacia]", "bmw", "KIA", "vw", "feat", "skoda", "lada", "audi", "ford", "Chevrolett"]
german_cars = ["bmw", "vw", "audi"]

for car in all_cars:
    if car in german_cars:
        print(car.title() + " is German cars")
    else:
        print(car.upper() + " is not German cars")