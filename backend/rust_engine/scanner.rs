// backend/rust_engine/scanner.rs

use std::fs::{self, File};
use std::io::{BufReader, Read};
use std::path::Path;
use std::fs::OpenOptions;
use std::io::Write;

const SIGNATURES: [&str; 3] = ["mal_sig_1", "virus123", "trojan.exe"];

pub fn scan_directory<P: AsRef<Path>>(path: P) {
    let entries = fs::read_dir(path).unwrap();
    for entry in entries {
        let entry = entry.unwrap();
        let path = entry.path();
        if path.is_dir() {
            scan_directory(path);
        } else {
            scan_file(path);
        }
    }
}

fn scan_file<P: AsRef<Path>>(file_path: P) {
    let path_str = file_path.as_ref().to_str().unwrap();
    let file = match File::open(&file_path) {
        Ok(f) => f,
        Err(_) => return,
