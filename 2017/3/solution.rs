fn main() {
    let target = 361527;
    let mut mat = vec![vec![0; 1001]; 1001];
    let dr : [i32; 4]= [-1, 0, 1, 0];
    let dc : [i32; 4]= [0, -1, 0, 1];
    let mut r : i32 = 500;
    let mut c : i32 = 500;
    mat[r as usize][c as usize] = 1;

    let ns = |r : i32, c : i32, mat : &Vec<Vec<i32>> | {
        let mut s = 0;
        for dr in [-1, -0, 1].iter() {
            for dc in [-1, 0, 1].iter() {
                if *dr == 0 && *dc == 0 {
                    continue;
                }
                let rr = r + *dr;
                let cc = c + *dc;
                let x = mat[rr as usize][cc as usize];
                s += x;
            }
        }
        return s;
    };

    let mut num;
    let mut rad = 2;
    loop {
        c += 1;
        num = ns(r, c, &mat);
        if num > target {
            println!("{}", num);
            return;
        }
        for d in 0..4 {
            let b = if d == 0 { rad - 1 } else { rad };
            for _ in 0..b {
                mat[r as usize][c as usize] = num;
                r = r + dr[d];
                c = c + dc[d];
                num = ns(r, c, &mat);
                if num > target {
                    println!("{} {} {}", r, c, num);
                    return;
                }
            }
        }
        mat[r as usize][c as usize] = num;
        rad += 2;
    }
}
