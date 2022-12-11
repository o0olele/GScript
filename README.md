# GScript
A game script built with python, using opencv.

(more features in developing)

# Requirements
~~~shell
pip install numpy opencv-contrib-python pywin32 Pillow pure-pthon-adb
~~~

# Usages
- Test for AzurLane
  - Set the window name to 'BlueStacks'
  - using func `WinScript()`
  - run main.py
    ~~~shell
    python main.py
    ~~~
  - when detected the 'attack again' button, click it.
    ~~~shell
    [('attack_again', (933, 761))]
    [('all_retire', (767, 811))]
    [('confirm', (1115, 779))]
    [('confirm', (1115, 779))]
    ~~~~

- Test for AzurLane using adb
  - Set the adb path
  - run main.py
    ~~~shell
    python main.py
    ~~~
