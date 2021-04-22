use std::{collections::HashMap, error::Error, fs::read_to_string};

fn main() -> Result<(), Box<dyn Error>> {
    let data = read_to_string("input")?;
    let dirs: Vec<&str> = data.trim().split(',').collect();
    let mut map = HashMap::new();

    map.insert("n", (0.0, 1.0));
    map.insert("s", (0.0, -1.0));
    map.insert("nw", (0.5, 0.5));
    map.insert("sw", (0.5, -0.5));
    map.insert("ne", (-0.5, 0.5));
    map.insert("se", (-0.5, -0.5));

    let mut x = 0f32;
    let mut y = 0f32;
    let mut m = 0f32;
    for d in dirs.iter() {
        let (dx, dy) = map.get(d).unwrap();
        x += dx;
        y += dy;
        m = m.max(x.abs() + y.abs())
    }
    println!("{}", m);
    Ok(())
}
