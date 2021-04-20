use std::collections::HashMap;
use std::fs::read_to_string;

fn main() {
    let lines: Vec<String> = read_to_string("input")
        .unwrap()
        .split('\n')
        .filter(|x| x.len() != 0)
        .map(|x| String::from(x))
        .collect();

    let mut map = HashMap::new();
    let mut m = 0;
    for line in lines.iter() {
        let tokens: Vec<&str> = line.split_whitespace().collect();
        let amount = tokens[2].parse::<i32>().unwrap();
        let check = tokens[6].parse::<i32>().unwrap();
        let t4 = *map.entry(tokens[4]).or_insert(0);
        let t0 = map.entry(tokens[0]).or_insert(0);

        match tokens[5] {
            ">" => (|| {
                if t4 > check {
                    if tokens[1] == "dec" {
                        *t0 -= amount;
                    } else {
                        assert_eq!(tokens[1], "inc");
                        *t0 += amount;
                    }
                }
            })(),
            ">=" => (|| {
                if t4 >= check {
                    if tokens[1] == "dec" {
                        *t0 -= amount;
                    } else {
                        assert_eq!(tokens[1], "inc");
                        *t0 += amount;
                    }
                }
            })(),
            "<" => (|| {
                if t4 < check {
                    if tokens[1] == "dec" {
                        *t0 -= amount;
                    } else {
                        assert_eq!(tokens[1], "inc");
                        *t0 += amount;
                    }
                }
            })(),
            "<=" => (|| {
                if t4 <= check {
                    if tokens[1] == "dec" {
                        *t0 -= amount;
                    } else {
                        assert_eq!(tokens[1], "inc");
                        *t0 += amount;
                    }
                }
            })(),
            "==" => (|| {
                if t4 == check {
                    if tokens[1] == "dec" {
                        *t0 -= amount;
                    } else {
                        assert_eq!(tokens[1], "inc");
                        *t0 += amount;
                    }
                }
            })(),
            "!=" => (|| {
                if t4 != check {
                    if tokens[1] == "dec" {
                        *t0 -= amount;
                    } else {
                        assert_eq!(tokens[1], "inc");
                        *t0 += amount;
                    }
                }
            })(),
            _ => assert!(false),
        }

        for (_, value) in &map {
            if *value > m {
                m = *value;
            }
        }
    }

    println!("{}", m);
}
