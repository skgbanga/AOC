use std::{
    collections::HashMap,
    fs::File,
    io::{BufRead, BufReader},
};

fn main() {
    let filename = "input";
    let file = File::open(filename).unwrap();
    let lines: Vec<String> = BufReader::new(file)
        .lines()
        .map(|x| x.expect("error"))
        .collect();

    let mut parent = HashMap::new();
    let mut weights = HashMap::new();
    let mut leaves = Vec::new();
    let mut children = HashMap::new();

    for line in lines.iter() {
        let tokens: Vec<&str> = line.split_whitespace().collect();
        let node = tokens[0];
        let weight: i32 = tokens[1][1..tokens[1].len() - 1].parse().unwrap();
        weights.insert(node, weight);
        if tokens.len() == 2 {
            leaves.push(node);
        } else if tokens.len() > 2 {
            let mut childs = Vec::new();
            for i in 3..tokens.len() {
                let mut child = tokens[i];
                if i != tokens.len() - 1 {
                    child = &child[..child.len() - 1];
                }
                childs.push(child);
                parent.insert(child, node);
            }
            children.insert(node, childs);
        } else {
            assert!(false);
        }
    }

    let mut child = leaves[0];
    let root;
    loop {
        if !parent.contains_key(&child) {
            root = child;
            break;
        }
        child = parent.get(child).unwrap();
    }

    fn check_balance(
        node: &str,
        graph: &HashMap<&str, Vec<&str>>,
        weights: &HashMap<&str, i32>,
    ) -> i32 {
        if !graph.contains_key(node) {
            return *weights.get(node).unwrap();
        }

        let w = *weights.get(node).unwrap();
        let vec: Vec<i32> = graph
            .get(node)
            .unwrap()
            .iter()
            .map(|x| check_balance(x, graph, weights))
            .collect();

        let cw: Vec<i32> = graph
            .get(node)
            .unwrap()
            .iter()
            .map(|x| *weights.get(x).unwrap())
            .collect();

        if vec.iter().min() != vec.iter().max() {
            println!(
                "Imbalance found at {} with weight {}. children {:?} {:?}",
                node, w, vec, cw
            );
        }

        return w + vec.iter().sum::<i32>();
    }

    check_balance(root, &children, &weights);
}
