use regex::Regex;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() -> std::io::Result<()> {
    let input_file = File::open("input.txt")?;
    let reader = BufReader::new(input_file);
    let lines = reader.lines();

    let re =
        Regex::new(r"^(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)$").unwrap();

    let mut total_part1 = 0;
    let mut total_part2 = 0;
    for line in lines {
        let line = &line.unwrap();
        let caps = re.captures(line).unwrap();
        let min = caps.name("min").unwrap().as_str().parse::<i32>().unwrap();
        let max = caps.name("max").unwrap().as_str().parse::<i32>().unwrap();
        let letter = caps.name("letter").unwrap().as_str();
        let password = caps.name("password").unwrap().as_str();

        let count = password.matches(letter).count() as i32;
        if (count >= min) && (count <= max) {
            total_part1 = total_part2 + 1;
        }

        let pos1 = min as usize;
        let pos2 = max as usize;
        let password_bytes = password.as_bytes();
        let letter_char = letter.as_bytes()[0] as char;
        let at_pos1 = password_bytes[pos1 - 1] as char;
        let at_pos2 = password_bytes[pos2 - 1] as char;
        if ((at_pos1 == letter_char) && (at_pos2 != letter_char))
            || ((at_pos1 != letter_char) && (at_pos2 == letter_char))
        {
            total_part2 = total_part2 + 1;
        }
    }

    println!("{}", total_part1);
    println!("{}", total_part2);

    Ok(())
}
