use std::collections::HashMap;

fn print_type<T>(_: &T) {
    println!("{}", std::any::type_name::<T>());
}


fn main() {
    let vec = vec![1, 2, 3, 4];
    let m = vec.iter().enumerate().max_by_key(|&(a, b)| (b, a));
    println!("{:?}", m.unwrap());
}
