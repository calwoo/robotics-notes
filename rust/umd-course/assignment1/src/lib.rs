/// A function that doubles a `i32` integer. The returned value is an `i32` integer.
pub fn double_v1(n: i32) -> i32 {
    2 * n
}

///
pub fn double_v2(n: &i32) -> i64 {
    let ret: i32 = 2 * n;
    ret as i64
}

///
pub fn double_v3(n: &mut i32) {
    *n *= 2;
}

const OUTSIZE: usize = 5;
pub fn fibonacci(ns: (i32, i32)) -> [i32; OUTSIZE] {
    let (mut n1, mut n2) = ns;
    let mut fib: [i32; OUTSIZE] = [0; OUTSIZE];

    for i in 0..OUTSIZE {
        fib[i] = n1 + n2;
        n1 = n2;
        n2 = fib[i];
    }

    fib
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_double_v1() {
        assert_eq!(double_v1(2), 4);
        assert_eq!(double_v1(-3), -6);
    }

    #[test]
    fn test_double_v2() {
        assert_eq!(double_v2(&5), 10);
    }

    #[test]
    fn test_double_v3() {
        let mut x: i32 = 2;
        double_v3(&mut x);
        assert_eq!(x, 4);
    }

    #[test]
    fn test_fibonacci() {
        assert_eq!(fibonacci((1, 1)), [2, 3, 5, 8, 13]);
    }
}
