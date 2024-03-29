from src.settings import *
import os 
import subprocess
import time 
import pyautogui
import random


def get_window_position(window_name):
    window = pyautogui.getWindowsWithTitle(window_name)[0]
    if window: 
        return window._rect.x, window._rect.y
    else:
        return False, False
    

def open_game():
    """Open game and click play button"""
    # Open game exe
    os.chdir(game_folder)
    subprocess.Popen(game_exe)
    
    # Find game window
    time.sleep(15)
    x,y = get_window_position("Nifty Island Launcher")
    print("Found game window at: ",x, y)
    
    # click play button in launcher
    pyautogui.click(x+window_w/2, y+window_h/2+30)
    print("Clicked play button")

    # check if game client is running 
    time.sleep(5)
    x, y = get_window_position("NiftyIsland") 
    if x: 
        print("Open game client success")
        return True
    else:
        print("Open game client error")
        return False
    


def close_game():
    """Close game"""
    os.system(f'taskkill /f /im "Nifty Island Launcher.exe"')
    os.system(f'taskkill /f /im "NiftyIslandClient.exe"')
    print("Closed Game success.")



def focus_game():
    x, y = get_window_position("NiftyIsland") 
    pyautogui.click(x+window_w/2, y+window_h/2)



def create_match():
    """Create match and auto start"""
    focus_game()
    pyautogui.press("g")
    # 894, 376
    x,y = get_window_position("NiftyIsland")
    pyautogui.click(x+894, y+376)
    print("Create match success")

    time.sleep(30)
    pyautogui.press("y")
    print("Start match success")



def auto_accept_match():
    """Auto accept new match"""
    focus_game()
    while True:
        pyautogui.press("y")
        time.sleep(random.randint(10,15))
        auto_move()



def auto_move(direction="w"):
    """Random move to prevent disconnect game wasd"""
    focus_game()
    with pyautogui.hold(direction):
        pyautogui.sleep(1)



def go_to_island(island_url):
    command  = "start msedge {}".format(island_url) 
    os.system(command)

