import time
import os
import zipfile

source = ['"/home/lich/Desktop/Команды Линукс"']
target_dir = '/home/lich/Desktop/backups'
yesterday = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = input('Введите комментарий ==> ')
if len(comment) == 0:
    target = yesterday + os.sep + now + '.zip'
else:
    target = yesterday + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(yesterday):
    os.mkdir(yesterday)
    print('Каталог успешно создан', yesterday)

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Рерваня копия успешно создана', target)
else:
    print('Создание резервной копии не удалось')