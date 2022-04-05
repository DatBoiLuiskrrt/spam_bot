# Automated text messaging


# import relevant modules
import time
import pyautogui

def SendMessage():
    time.sleep(4)
    text = open('text.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')

SendMessage()