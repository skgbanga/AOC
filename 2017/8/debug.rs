use std::fs::File;
use std::io;
use std::io::Read;

#[allow(dead_code)]
fn read_contents1() -> Result<String, io::Error> {
    let mut f = match File::open("input") {
        Ok(f) => f,
        Err(error) => return Err(error),
    };
    let mut s = String::new();
    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),
        Err(error) => Err(error),
    }
}

fn read_contents2() -> Result<String, io::Error> {
    let mut f = File::open("input")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}

fn read_contents3() -> Result<String, io::Error> {
    let mut s = String::new();
    File::open("input")?.read_to_string(&mut s)?;
    Ok(s);
}

fn main() {
    let _ = read_contents2();
}
