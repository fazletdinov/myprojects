cars = ['bmw', 'ws', 'feat', 'skoda', 'lada']

for car in cars:
    print(car.upper())

for x in range(0, 10):
    print(x)

mynumber_list = list(range(0, 10))
print(mynumber_list)
print("======================================")
for x in mynumber_list:
    x = x * 2
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number is: " + str(max(mynumber_list)))

print("Min number is: " + str(min(mynumber_list)))

print("Sum of list is: " + str(sum(mynumber_list)))

print("=====================================")

cars = ['bmw', 'ws', 'feat', 'skoda', 'lada']
mycars = cars[1:4]
print(mycars)

mycars2 = cars[:4]
print(mycars2)

mycars3 = cars[-3:]
print(mycars3)

print("======================================")

cars = ['bmw', 'ws', 'feat', 'skoda', 'lada']
mycars = cars[:] # копировать массив ( изменения на массиве cars не будут влиять на массив mycars