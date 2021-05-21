use std::fs::read_to_string;

fn main() {
    let line = read_to_string("input").unwrap();
    let input = line.trim();
    let mut data: Vec<char> = "abcdefghijklmnop".chars().collect();
    let l = data.len();
    for token in input.split(",") {
        let ch = token.chars().next().unwrap();
        match ch {
            's' => {
                let w: usize = token[1..].parse().unwrap();
                assert!(w < l);
                data.rotate_left(l - w);
            }
            'x' => {
                let bs: Vec<usize> = token[1..]
                    .split("/")
                    .map(|x| x.parse::<usize>().unwrap())
                    .collect();
                data.swap(bs[0], bs[1]);
            }
            'p' => {
                let bs: Vec<char> = token[1..]
                    .split("/")
                    .map(|x| x.chars().next().unwrap())
                    .collect();
                let i = data.iter().position(|&x| x == bs[0]).unwrap();
                let j = data.iter().position(|&x| x == bs[1]).unwrap();
                data.swap(i, j);
            }
            _ => panic!("Can't reach here"),
        }
    }

    let s: String = data.iter().collect();
    println!("{}", s);
}
