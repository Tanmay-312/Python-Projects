import pyautogui as pg
import time

# Giving Delay to run program
print("program will run after 5 second")
time.sleep(5)
print("running")

for i in range(10):
    # writing the messages
    pg.write("I love you")
    time.sleep(0)
    # Sending the messages by pressing enter
    pg.press("Enter")