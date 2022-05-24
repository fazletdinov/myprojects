cities = ['New York', 'Moscow', 'new dehli', 'Simfiropol', 'Toronto']
print(cities)
print(len(cities))
print(cities[0])
print(cities[-1])
print(cities[2].title())
print(cities[1].upper())
print(cities[3].lower())

print(cities)

cities [2]='Tula'
print(cities)

cities.append('Kursk')
cities.append('Yalta')
print(cities)
cities.insert(2, 'Feodosia')
print(cities)

del cities[-2]
print(cities)

cities.remove('Tula')
print(cities)

deleted_city = cities.pop()
print('Deleted city is: ' + deleted_city)
print(cities)

cities.sort()
print(cities)

cities.reverse()
print(cities)