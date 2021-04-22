use std::cmp;
use std::collections::HashMap;
use std::error::Error;
use std::fs::read_to_string;

fn main() -> Result<(), Box<dyn Error>> {
    let lines: Vec<String> = read_to_string("input")?
        .split('\n')
        .filter(|x| x.len() != 0)
        .map(String::from)
        .collect();

    let mut map = HashMap::new();
    let mut m = 0;
    for line in lines.iter() {
        let tokens: Vec<&str> = line.split_whitespace().collect();
        let amount = tokens[2].parse::<i32>()?;
        let check = tokens[6].parse::<i32>()?;
        let t4 = *map.entry(tokens[4]).or_insert(0);
        let t0 = map.entry(tokens[0]).or_insert(0);

        let mut call = |cmp: fn(i32, i32) -> bool| {
            if cmp(t4, check) {
                if tokens[1] == "dec" {
                    *t0 -= amount;
                } else {
                    assert_eq!(tokens[1], "inc");
                    *t0 += amount;
                }
            }
            m = cmp::max(m, *t0);
        };

        match tokens[5] {
            ">" => call(|a, b| a > b),
            ">=" => call(|a, b| a >= b),
            "<" => call(|a, b| a < b),
            "<=" => call(|a, b| a <= b),
            "==" => call(|a, b| a == b),
            "!=" => call(|a, b| a != b),
            _ => assert!(false),
        }
    }

    println!("{}", m);
    Ok(())
}
