use std::collections::{HashMap, HashSet, VecDeque};
use std::error::Error;
use std::fs::read_to_string;

fn main() -> Result<(), Box<dyn Error>> {
    let data = read_to_string("input")?;
    let mut graph = HashMap::new();
    for line in data.split('\n').filter(|x| x.len() != 0) {
        let tokens: Vec<&str> = line.split("<->").map(|x| x.trim()).collect();
        let node = tokens[0].parse::<i32>().unwrap();
        let nums: Vec<i32> = tokens[1]
            .split(',')
            .map(|x| x.trim().parse::<i32>().unwrap())
            .collect();

        graph.insert(node, nums);
    }

    let mut g = 0;
    let mut seen = HashSet::new();
    let mut d = VecDeque::new();
    for node in graph.keys() {
        if !seen.contains(&node) {
            d.push_back(node);
            seen.insert(node);
            while d.len() != 0 {
                let n = d.pop_front().unwrap();
                for ns in graph.get(n).unwrap().iter() {
                    if !seen.contains(&ns) {
                        d.push_back(ns);
                        seen.insert(ns);
                    }
                }
            }
            g += 1;
        }
    }
    println!("{}", g);
    Ok(())
}
