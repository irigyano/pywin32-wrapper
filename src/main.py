import win32gui
import win32con
import win32api
import time
from VK_CODE import VK_CODE


class Win32:
    def __init__(self, hwnd) -> None:
        self.hwnd = hwnd

    def focus_window(self):
        # some program require focus to interact e.g chrome/discord
        win32gui.SetForegroundWindow(self.hwnd)
        time.sleep(0.1)

    def left_click(self, x, y):
        pos_long = win32api.MAKELONG(x, y)
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN,
                             0x01, pos_long)
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP,
                             0x01, pos_long)

    def keyboard_event(self, key):
        hex = VK_CODE[key]

        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, hex, 0)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, hex, 0)
        # SendMessage not working in chrome
        # win32api.SendMessage()

    def keyboard_input(self, key):
        hex = VK_CODE[key]
        win32api.SendMessage(self.hwnd, win32con.WM_CHAR, hex, 0)


TARGET_WINDOW_NAME = "@rinoyagi - Discord"

if __name__ == '__main__':
    hwnd = win32gui.FindWindow(None, TARGET_WINDOW_NAME)
    if hwnd:
        window = Win32(hwnd)
        # window.focus_window()
        # actions here

    else:
        # print available windows
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hwnd, win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)
