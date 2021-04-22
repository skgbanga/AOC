use std::env;
use std::fs::read_to_string;

fn main() {
    let args: Vec<String> = env::args().collect();
    let input = read_to_string(&args[1]).unwrap();
    let data = input.trim();
    let mut score = 0;
    let mut skip = false;
    let mut depth = 1;
    let mut garbage = false;
    let mut noncan = 0;
    for (_, ch) in data.chars().enumerate() {
        if skip {
            skip = false;
            continue;
        }
        if garbage {
            match ch {
                '>' => garbage = false,
                '!' => skip = true,
                _ => noncan += 1,
            }
            continue;
        }

        match ch {
            '{' => depth += 1,
            '}' => {
                depth -= 1;
                score += depth;
            }
            '<' => garbage = true,
            _ => (),
        }
    }
    println!("score = {}, noncan = {}", score, noncan);
}
