use std::{
    collections::HashMap,
    fs::File,
    io::{BufRead, BufReader},
};

fn main() {
    let filename = "input";
    let file = File::open(filename).unwrap();
    let vec: Vec<String> = BufReader::new(file)
        .lines()
        .map(|x| x.expect("error"))
        .collect();

    let line = &vec[0];
    let mut tokens: Vec<i32> = line
        .split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    let mut set = HashMap::new();
    let mut steps = 0;
    let n = tokens.len();
    loop {
        if set.contains_key(&tokens) {
            let prev = set.get(&tokens).unwrap();
            println!("Step taken to see a duplicate : {}", steps - prev);
            break;
        }
        set.insert(tokens.clone(), steps);

        // find index of max element
        let mut m = 0;
        let mut idx = 0;
        for (index, token) in tokens.iter().enumerate() {
            if m < *token {
                m = *token;
                idx = index;
            }
        }

        // distribute element to others
        tokens[idx] = 0;
        idx += 1;
        while m > 0 {
            tokens[idx % n] += 1;
            m -= 1;
            idx += 1;
        }

        steps += 1;
    }
}
