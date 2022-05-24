enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudilla',
}

all_enemys = []

for x in range(0, 10):
    all_enemys.append(enemy.copy())

for ene in all_enemys:
    print(ene)

all_enemys[6]['health'] = 30
print("======================")

for x in all_enemys:
    print(x)

all_enemys[9]['name'] = 'kasel'
all_enemys[9]['loc_x'] += 10
print('================')
for y in all_enemys:
    print(y)