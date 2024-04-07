from src.settings import *
import os 
import subprocess
import time 
import pyautogui
import random
pyautogui.FAILSAFE = False


def get_window_position(window_name):
    """Get window position x, y by it name"""
    windows = pyautogui.getWindowsWithTitle(window_name)
    if len(windows) > 0:
        return windows[0]._rect.x, windows[0]._rect.y
    else:
        return False, False
    

def is_game_running():
    """Check if game instance exists"""    
    # check if game client is running 
    windows = pyautogui.getWindowsWithTitle(name_client)
    windows2 = pyautogui.getWindowsWithTitle(name_launcher)

    if len(windows) > 0:
        return True 
    else:
        return False
    

def open_game():
    """Open game and click play button"""

    # check if game already opened
    if is_game_running():
        console.log("Game is running.. close it before open again")
        return
    
    # Open game exe
    os.chdir(game_folder)
    subprocess.Popen(game_exe)
    
    # Find game window
    time.sleep(15)
    x,y = get_window_position(name_launcher)
    console.log("Found game window at: ",x, y)
    
    # click play button in launcher
    pyautogui.click(x+window_w/2, y+window_h/2+30)
    console.log("Clicked play button")

    # check if game windows is running
    time.sleep(15)
    if is_game_running():
        console.log("Game is running")
    else:
        console.log("Open game failed")
    

def close_game():
    """Close game"""
    os.system(f'taskkill /f /im "Nifty Island Launcher.exe"')
    os.system(f'taskkill /f /im "NiftyIslandClient.exe"')
    console.log("Closed Game success.")


def focus_game():
    x, y = get_window_position(name_client) 
    pyautogui.click(x+window_w/2, y+window_h/2)


def create_match():
    """Create match and auto start"""
    focus_game()
    pyautogui.press("g")

    # 894, 376
    time.sleep(3)
    x,y = get_window_position(name_client)
    pyautogui.click(x+865, y+335)

    console.log("Create match success. Waiting other player join")

    time.sleep(30)
    focus_game()
    pyautogui.press("y")
    console.log("Start match success")


def close_match():
    """Close match after ending"""
    time.sleep(3)
    x,y = get_window_position(name_client)
    pyautogui.click(x+622, y+633) # Exit button
    pyautogui.click(x+133, y+638) # Rematch button
    console.log("Close match success")


def accept_match():
    """Auto accept new match"""
    if not is_game_running(): return
    focus_game()
    pyautogui.press("y")



def auto_move(direction="w"):
    """Random move to prevent disconnect game wasd"""
    if not is_game_running(): return
    console.log("Move ", direction)
    focus_game()
    with pyautogui.hold(direction):
        pyautogui.sleep(1)


def go_to_island(island_url):
    command  = "start msedge {}".format(island_url) 
    os.system(command)


def mouse_click(x, y):
    if not is_game_running(): return
    console.log("Click ", x, y)
    focus_game()
    pyautogui.click(x,y)


def chat():
    pass 


def random_click():
    pass 


def auto_chat():
    pass 


def send_notif():
    """Send notification to telegram app"""
    pass 