use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() -> std::io::Result<()> {
    let input_file = File::open("input.txt")?;
    let reader = BufReader::new(input_file);
    let lines = reader.lines();

    let mut missing_ids: Vec<i32> = (0..1025).collect();

    let mut max_id = -1;
    let mut min_id = 1025;
    for line in lines {
        let line = line.unwrap();

        let seat_id = i32::from_str_radix(
            line.replace("F", "0")
                .replace("B", "1")
                .replace("L", "0")
                .replace("R", "1")
                .as_str(),
            2,
        )
        .unwrap();

        if seat_id > max_id {
            max_id = seat_id
        }
        if seat_id < min_id {
            min_id = seat_id
        }

        missing_ids.retain(|&x| x != seat_id);
    }
    missing_ids.retain(|&x| (x < max_id) && (x > min_id));

    println!("{}", max_id);
    for missing_id in missing_ids {
        print!("{} ", missing_id);
    }
    println!();

    Ok(())
}
