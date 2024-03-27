import win32api
import keyboard

while True:
    keyboard.wait("ctrl")
    x, y = win32api.GetCursorPos()
    # dual monitor setup
    # if x < 0:
    #     x += 1920
    print(x, y)
