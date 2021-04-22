use std::fs::read_to_string;

fn main() {
    let line = read_to_string("input").unwrap();
    let mut data: Vec<u32> = line.trim().chars().map(|x| x as u32).collect();
    data.extend([17, 31, 73, 47, 23].iter());

    let mut nums: Vec<u32> = (0..256).collect();
    let idx = |x| (x % 256) as usize;
    let mut current: u32 = 0;
    let mut skip: u32 = 0;
    for _ in 0..64 {
        for len in data.iter() {
            let mut i = current;
            let mut j = current + len - 1;
            while i < j {
                nums.swap(idx(i), idx(j));
                i += 1;
                j -= 1;
            }
            current += len + skip;
            skip += 1;
        }
    }

    let mut s = String::new();
    let mut index = 0;
    while index < nums.len() {
        let mut n = nums[index];
        for i in index + 1..index + 16 {
            n = n ^ nums[i];
        }
        index += 16;
        s.push_str(&format!("{:02x}", n));
    }
    println!("{}", s);
}
