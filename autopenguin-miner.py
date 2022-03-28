from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
from pynput import keyboard
import time
from scipy.spatial.distance import euclidean

mouse = Controller()
keyboard = keyboard.Controller()
positions = []

def on_press(key):
    global positions
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        print('The current pointer position is {0}'.format(mouse.position))
        if key.char == 'a':
        	positions.append(mouse.position)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == Key.enter:
        # Stop listener
        return False

def move_to(pos):
    mouse.position = pos
    time.sleep(0.01)
    mouse.click(Button.left)
    time.sleep(0.8)
    keyboard.press('d')
    keyboard.release('d')

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

print('postions between: ' + str(positions[0]) + ' and ' + str(positions[1]))

i = 0
while(True):
    if (i > 2 and euclidean(mouse.position, positions[(i-1)%len(positions)]) > 100):
        break
    move_to(positions[i%len(positions)])
    i += 1
    time.sleep(11)
