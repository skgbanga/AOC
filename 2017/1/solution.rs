use std::{
    convert::TryInto,
    fs::File,
    io::{BufRead, BufReader},
};

fn part1(line: &str) -> i32 {
    // python code:
    //
    // s = sum(int(a) for a, b in zip(line, line[1:] + [line[0]]) if a == b)

    line.chars()
        .zip(line.chars().cycle().skip(1))
        .fold(0, |acc, (a, b)| {
            if a == b {
                acc + a.to_digit(10).expect("Could not convert char to digit")
            } else {
                acc
            }
        })
        .try_into()
        .expect("Failed to convert to i32")
}

fn part2(line: &str) -> i32 {
    let sum: i32 = line
        .chars()
        .zip(line.chars().skip(line.len() / 2))
        .fold(0, |acc, (a, b)| {
            if a == b {
                acc + a.to_digit(10).expect("Could not convert char to digit")
            } else {
                acc
            }
        })
        .try_into()
        .expect("Failed to convert to i32");

    sum * 2
}

fn main() {
    let filename = "input";
    let file = File::open(filename).unwrap();

    let vec = BufReader::new(file)
        .lines()
        .map(|line| line.expect("Could not read line from file"))
        .collect::<Vec<String>>();

    let line = &vec[0];
    println!("{}", part1(line));
    println!("{}", part2(line));
}
