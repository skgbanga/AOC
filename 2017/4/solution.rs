use std::{
    collections::HashSet,
    fs::File,
    io::{BufRead, BufReader},
};

fn main() {
    let filename = "input";
    let file = File::open(filename).unwrap();
    let lines = BufReader::new(file)
        .lines()
        .map(|line| line.expect("error"))
        .collect::<Vec<String>>();

    let mut s = 0;
    for line in lines.iter() {
        let mut vec = Vec::new();
        let mut set = HashSet::new();

        for token in line.split_whitespace() {
            let mut chars: Vec<char> = token.chars().collect();
            chars.sort();
            let ss: String = chars.into_iter().collect();
            vec.push(ss.clone());
            set.insert(ss);
        }
        if vec.len() == set.len() {
            s += 1;
        }
    }
    println!("{}", s);
}
