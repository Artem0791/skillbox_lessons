import time

seconds = int(input('Сколько секунд греть еду: '))
for sec in range(seconds, 0, -1):
    print('Осталось {} секунд'.format(sec))
    time.sleep(1)
print('Дзынь!')