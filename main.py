import rotatescreen
import time
import ctypes

screen = rotatescreen.get_primary_display()
for i in range(1000000000):
     time.sleep(1)
     screen.rotate_to(i*90 % 360)

ctypes.windll.user32.MessageBoxW(0, "I Screwed your Box ! HAHAHA", "RIP", 1)
