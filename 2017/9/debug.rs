fn identity(a: &str) {
    println!("{}", a);
}

fn main() {
    let a = 42;
    let b = identity(a);
    println!("{}", b);
}
