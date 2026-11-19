# Discord quest spoofer

A simple program that automatically grabs the list of games discord can detect, and automatically creates the required file structure for discords quest detection.

> ## ⚠️ This program puts your account at risk of being quest limited!
> I recommend using it in moderation, and if you get an "Unusual quest activity" warning from discord, not using the program for a while/at all.

## Usage

1. Download the latest release
2. Unzip and run the exe
3. Type in the name of the game (make sure it's spelled correctly, and is the full game title)
4. Click spoof

## Building from source
1. Clone the repo
2. **(Optional)** Build the dummy exe yourself  
```
cd dummy
cargo build --release
cd ..
```
4. Install dependancies `pip install -r requirements.txt`
5. Run `pyinstaller --onefile --name "Discord Quest Spoofer" --add-binary "dummy/target/release/dummy.exe;." main.py`


> ### ⚠️ May not work with all games! I recommend checking out r/DiscordQuests for any that do not work with this program
