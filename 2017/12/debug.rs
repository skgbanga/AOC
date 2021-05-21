fn main() {
    let seq: Vec<i32> = (0..10).collect();
    for &i in seq.iter() {
        println!("{}", i);
    }
}
