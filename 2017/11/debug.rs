trait Summary {
    fn sum(&self) -> String;
}

#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}

impl Summary for Point {
    fn sum(&self) -> String {
        format!("Summary {:?}", self)
    }
}

fn notify<T>(item: &T)
where
    T: Summary,
{
    println!("{}", item.sum());
}

fn main() {
    let p = Point { x: 10, y: 20 };
    notify(&p);
    println!("{:?}", p);
}
