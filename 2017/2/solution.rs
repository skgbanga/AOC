use std::{
    cmp,
    fs::File,
    io::{BufRead, BufReader},
};

fn part1(lines: &Vec<String>) {
    let mut s = 0;
    for line in lines.iter() {
        let mut max = 0;
        let mut min = 100_000;
        for token in line.split_whitespace() {
            let token = token.parse::<i32>().unwrap();
            max = cmp::max(max, token);
            min = cmp::min(min, token);
        }
        s += max - min;
    }
    println!("{}", s);
}

fn part2(lines: &Vec<String>) {
    fn handle(nums: &Vec<i32>) -> i32 {
        let len = nums.len();
        for i in 0..len {
            for j in i + 1..len {
                let a = cmp::min(nums[i], nums[j]);
                let b = cmp::max(nums[i], nums[j]);
                if b % a == 0 {
                    return b / a;
                }
            }
        }
        assert!(false);
        return 0;
    }

    let mut s = 0;
    for line in lines.iter() {
        let tokens = line
            .split_whitespace()
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();
        s += handle(&tokens);
    }
    println!("{}", s);
}

fn main() {
    let filename = "input";
    let file = File::open(filename).unwrap();

    let vec = BufReader::new(file)
        .lines()
        .map(|line| line.expect("error"))
        .collect::<Vec<String>>();

    part1(&vec);
    part2(&vec);
}
