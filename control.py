import easygui as eg

while True:
    direction = eg.buttonbox(msg='Which direction?',choices=('Left','Forward','Right'))
    if direction == 'Forward':
        print('Moving forward')
    elif direction == 'Left':
        print('Turning left')
    else:
        print('Turning right')
