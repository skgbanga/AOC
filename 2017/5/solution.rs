use std::{
    fs::File,
    io::{BufRead, BufReader},
};

fn main() {
    let filename = "input";
    let file = File::open(filename).unwrap();
    let mut nums: Vec<i32> = BufReader::new(file)
        .lines()
        .map(|x| x.unwrap().parse::<i32>().unwrap())
        .collect();

    let n = nums.len() as i32;
    let mut ip: i32 = 0;
    let mut steps = 0;
    while ip < n {
        let tmp = nums[ip as usize];
        if tmp >= 3 {
            nums[ip as usize] -= 1
        } else {
            nums[ip as usize] += 1
        }
        ip += tmp;
        steps += 1;
    }
    println!("{}", steps);
}
