use std::io;
use std::ops::RangeInclusive;
use std::str::FromStr;

fn contains_fully<T: PartialOrd>(left: RangeInclusive<T>, right: RangeInclusive<T>) -> bool {
    left.contains(right.start()) && left.contains(right.end()) || (right.contains(left.start()) && right.contains(left.end()))
}

fn overlaps<T: PartialOrd>(left: RangeInclusive<T>, right: RangeInclusive<T>) -> bool {
    left.contains(right.start()) || left.contains(right.end())
    || right.contains(left.start()) || right.contains(left.end())
}

fn part1(input: Vec<String>) -> i32 {
    input
        .iter()
        .map(|line|
            line
                .replace("-", ",")
                .split(",")
                .map(usize::from_str)
                .map(|x| x.unwrap()).collect::<Vec<usize>>())
        .map(|v| (v[0]..=v[1], v[2]..=v[3]))
        .map(|(left, right)| contains_fully(left, right))
        .map(i32::from)
        .sum()
}

fn part2(input: Vec<String>) -> i32 {
    input
        .iter()
        .map(|line|
            line
                .replace("-", ",")
                .split(",")
                .map(usize::from_str)
                .map(|x| x.unwrap()).collect::<Vec<usize>>())
        .map(|v| (v[0]..=v[1], v[2]..=v[3]))
        .map(|(left, right)| overlaps(left, right))
        .map(i32::from)
        .sum()
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let input: Vec<String> = stdin.lines().map(|x| x.unwrap()).collect();

    let total1: i32 = part1(input.clone());
    let total2: i32 = part2(input);

    println!("{}", total1);
    println!("{}", total2);

    Ok(())
}
