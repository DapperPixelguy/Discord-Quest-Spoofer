import requests, json, os, shutil, subprocess, sys, re
import tkinter as tk

DISCORD_DISCOVERY_API = "https://discord.com/api/v9/games/detectable"

def bundled(name):
    """Path to a file packed inside the exe (or next to the script when not built)."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)

def app_dir():
    """Folder the exe (or script) actually lives in."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

DUMMY = bundled("dummy.exe")

BASE_DIR = os.path.join(app_dir(), "Games")
CACHE_FILE = os.path.join(app_dir(), "cache.json")
os.makedirs(BASE_DIR, exist_ok=True)

def check_detectable():
    if os.path.isfile(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)

    response = requests.get(DISCORD_DISCOVERY_API, timeout=30)
    response.raise_for_status()
    data = response.json()

    with open(CACHE_FILE, "w") as f:
        f.write(json.dumps(data))

    return data

def safe_folder_name(name):
    """Strip characters Windows doesn't allow in folder names."""
    return re.sub(r'[<>:"/\\|?*]', "", name).strip().rstrip(".")

def find_game(data, game_name):
    for game in data:
        if game["name"].lower() == game_name.lower():
            game_data = game
            return game_data
    return None

def find_game_path(game):
    """Find the first game path that is for Windows, and is not a launcher"""
    for exe in game.get("executables") or []:
        if exe.get("os") == "win32" and not exe.get("is_launcher", False):
            return exe['name']


def fake_game(game_name: str):
    data = check_detectable()

    game = find_game(data, game_name)
    if not game:
        feedback.config(text="Game not found")
        return

    exe_rel = find_game_path(game)
    if not exe_rel:
        feedback.config(text="Unable to find a Windows, non-launcher executable.")
        return

    dest = os.path.normpath(
        os.path.join(BASE_DIR, safe_folder_name(game['name']), exe_rel)
    )

    os.makedirs(os.path.dirname(dest), exist_ok=True)

    if not os.path.exists(dest):
        shutil.copy(DUMMY, dest)

    subprocess.Popen([dest], creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("300x150")
    label = tk.Label(root, text="Game Name")
    label.pack()
    entry = tk.Entry(root, justify=tk.CENTER)
    entry.pack()
    enter = tk.Button(root, text="Spoof", command=lambda: fake_game(entry.get()))
    enter.pack()
    feedback = tk.Label(root)
    feedback.pack()
    root.mainloop()


    # while True:
    #     game = input("Game name: ")
    #     fake_game(game)