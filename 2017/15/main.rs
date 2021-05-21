struct Gen {
    start: i64,
    mult: i64,
    mo: i64,
}

impl Gen {
    fn next(&mut self) -> u16 {
        loop {
            let p = (self.start * self.mult) % 2147483647;
            self.start = p;
            if p % self.mo == 0 {
                return p as u16;
            }
        }
    }
}

fn main() {
    let mut g1 = Gen {
        start: 512,
        mult: 16807,
        mo: 4,
    };
    let mut g2 = Gen {
        start: 191,
        mult: 48271,
        mo: 8,
    };

    let mut cnt = 0;
    let mut s = 0;
    while cnt < 5_000_000 {
        let a1 = g1.next();
        let a2 = g2.next();
        if a1 == a2 {
            s += 1;
        }
        cnt += 1;
    }
    println!("{}", s);
}
