use std::collections::HashSet;
use std::fs;

fn main() -> std::io::Result<()> {
    let _answers = fs::read_to_string("input.txt")?;
    let answers = _answers.trim().split("\n\n").collect::<Vec<&str>>();

    let total_part1 = answers
        .iter()
        .map(|s| {
            s.split_whitespace()
                .collect::<String>()
                .chars()
                .collect::<HashSet<char>>()
                .len()
        })
        .sum::<usize>();

    let total_part2 = answers
        .iter()
        .map(|s| {
            let group = s
                .split("\n")
                .map(|t| t.chars().collect())
                .collect::<Vec<Vec<char>>>();

            let mut questions: HashSet<&char> = group.iter().flatten().collect();
            for person in group.iter() {
                questions.retain(|k| person.contains(k));
            }
            questions.len()
        })
        .sum::<usize>();

    println!("{}", total_part1);
    println!("{}", total_part2);

    Ok(())
}
