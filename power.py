from gpiozero import Button
from signal import pause
import os

switch = Button(17)

def execute_script():
    print("Switch activated! Executing script...")
    os.system("/path/to/your/script.sh")

switch.when_pressed = execute_script

pause()
