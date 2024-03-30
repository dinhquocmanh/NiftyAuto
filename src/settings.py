from rich.console import Console 
console = Console()

game_folder = "C:\\Program Files (x86)\\Nifty Island"
game_exe = "Nifty Island Launcher.exe"
game_process = "Nifty Island Launcher.exe"
game_client = "NiftyIslandClient.exe"

name_client = "NiftyIsland"
name_launcher = "Nifty Island Launcher"

window_w = 1152
window_h = 648

MENU = """1. List all clients
2. Select client [1-10]
3. Select all client
"""

MENU_CLIENT = """1. Open game
2. Close game
3. Start AutoMove
4. Auto host match
5. Auto accept match
6. Go to Island
"""

MENU_ALL = """1. Open game all
2. Close game all 
3. Start AutoMove
4. All go to 1 Island
"""

VPS = {
    "vpsgpu01":	"222.255.117.251",
    "vpsgpu02":	"222.255.117.229",
    "vpsgpu03":	"222.255.117.210",
    "vpsgpu04":	"222.255.117.206",
    "vpsgpu05":	"222.255.117.198",
    "vpsgpu06":	"103.90.227.250",
    "vpsgpu07":	"103.90.227.217",
    "vpsgpu08":	"103.90.227.200",
    "vpsgpu09":	"103.90.227.188",
    "vpsgpu10":	"103.90.227.183",
}

HOST_IP = "103.82.27.237"
HOST_PORT = 11705