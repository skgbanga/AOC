// use std::collections::HashMap;

// fn print_type<T>(_: &T) {
//     println!("{}", std::any::type_name::<T>());
// }

fn main() {
    let add = |a: i32, b: i32| a + b;
    let sub = |a: i32, b: i32| a - b;
    println!("{}", add(3, 2));
    println!("{}", sub(3, 2));
}
