use std::fs::read_to_string;

fn main() {
    let vec: Vec<String> = read_to_string("input2")
        .unwrap()
        .split('\n')
        .filter(|x| x.len() != 0)
        .map(|x| String::from(x))
        .collect();

    for line in vec.iter() {
        println!("{}", line);
    }
}
