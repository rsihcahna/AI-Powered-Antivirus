// backend/rust_engine/main.rs

mod scanner;

use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("Usage: antivirus <directory_path>");
        return;
    }

    let dir_path = &args[1];
    println!("🔍 Scanning directory: {}", dir_path);

    scanner::scan_directory(dir_path);

    println!("✅ Scan completed.");
}
