#Creator: Nathan A
#Date: 7/6/20
#Description: Auto Runner/Walker

from pynput.keyboard import Key, Controller
import keyboard
import time
keyboard1 = Controller();
print ('type "help()" to see all options Or check out our wiki "https://github.com/Nate-Ar/Automator/wiki"')

while True:
    try:
        input1 = input('> ');
        if input1 == 'walk()':
            walk();

        if input1  == 'run()':
            run();

        if input1 == 'quit()':
            break

        if input1 == 'help()':
            print ('Try "run()","walk()","quit()"')
            print ('If your walk/run wont stop the click "W" or "Shift W"')


        def run():
            print('Press "L" to stop');
            time.sleep(5)
            while True:
                try:
                    keyboard1.press(Key.shift_l);
                    keyboard1.press('w');
                    if keyboard.is_pressed('l'):
                        keyboard1.release('w')
                        keyboard1.release(Key.shift_l);
                        quit()
                except:
                    break

        def walk():
            print('Press "L" to stop');
            time.sleep(5)
            while True:
                try:
                    keyboard1.press('w');
                    if keyboard.is_pressed('l'):
                        keyboard1.release('w')
                        quit()
                except:
                    break

    except:
        print ('sorry something went wrong please click enter a few times and try again ')
        continue
