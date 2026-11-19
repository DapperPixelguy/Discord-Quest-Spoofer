use std::thread;
use std::time::Duration;

fn main() {
    println!("pretending to be a game, close this window to stop");
    loop {
        thread::sleep(Duration::from_secs(60));
    }
}