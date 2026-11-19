# Discord quest spoofer

A simple program that automatically grabs the list of games discord can detect, and automatically creates the required file structure for discords quest detection.

> ## ⚠️ This program puts your account at risk of being quest limited!
> I recommend using it in moderation, and if you get an "Unusual quest activity" warning from discord, not using the program for a while/at all.

## Usage

1. Download the zip from the [latest release](https://github.com/<you>/<repo>/releases/latest)
2. Unzip it and run the exe from inside the folder. Windows may say "Windows protected your PC" because the exe isn't signed. Click **More info → Run anyway**
3. Type in the game's full name as Discord lists it (capitals don't matter)
4. Click **Spoof**. A dummy window will open, and Discord should pick up the game within a few seconds
5. Close the dummy window to stop

> **⚠️ May not work with all games! I recommend checking out r/DiscordQuests for any that do not work with this program**

## Antivirus warning
Some antivirus programs flag this as suspicious, because it copies exes and runs them, and because PyInstaller exes often get false positives. The full source, including the dummy, is in this repo, so you can check it or build it yourself (below).

## Building from source
1. Clone the repo
2. **(Optional)** Build the dummy exe yourself  
```
cd dummy
cargo build --release
cd ..
```
4. Install dependancies `pip install -r requirements.txt`
5. Run `pyinstaller --noconsole --name "Discord Quest Spoofer" --add-binary "dummy/target/release/dummy.exe;." main.py`
6. The build will be available in `dist/`


## Todo
1. Upgrade GUI
2. Add a way to quickly launch multiple games at the same time for the games/hours played badge


