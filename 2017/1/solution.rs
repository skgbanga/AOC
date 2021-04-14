use std::fs::File;
use std::io::{BufRead, BufReader};

fn part1(line: &str) -> i32 {
    // python code:
    // 
    // s = sum(int(a) for a, b in zip(line, line[1:] + [line[0]]) if a == b)

    let other = &line[1..];
    let mut s = 0;
    for (a, b) in line.chars().zip(other.chars()) {
        if a == b {
            s += a.to_digit(10).unwrap() as i32;
        }
    }
    let first = line.chars().next().unwrap();
    let last = line.chars().rev().next().unwrap();
    if first == last {
        s += first.to_digit(10).unwrap() as i32;
    }
    return s;
}

fn part2(line: &str) -> i32 {
    let len = line.len();
    let other = &line[len / 2..];
    let mut s = 0;
    for (a, b) in line.chars().zip(other.chars()) {
        if a == b {
            s += a.to_digit(10).unwrap() as i32;
        }
    }
    return s * 2;
}

fn main() {
    let filename = "input";
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    let mut vec = Vec::new();
    for line in reader.lines() {
        let line = line.unwrap();
        vec.push(line);
    }

    let line = &vec[0];
    println!("{}", part1(line));
    println!("{}", part2(line));
}
