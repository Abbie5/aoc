use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() -> std::io::Result<()> {
    let input_file = File::open("input.txt")?;
    let reader = BufReader::new(input_file);
    let lines = reader.lines();

    let mut missing_ids: Vec<i32> = (0..1025).collect();

    let mut max_id = -1;
    for line in lines {
        let line = line.unwrap();

        let mut row_num = 0;
        for (index, character) in line.get(0..7).unwrap().chars().enumerate() {
            match character {
                'F' => continue,
                'B' => row_num += 2i32.pow(6 - index as u32),
                _ => panic!("unrecognised character"),
            }
        }

        let mut col_num = 0;
        for (index, character) in line.get(7..10).unwrap().chars().enumerate() {
            match character {
                'L' => continue,
                'R' => col_num += 2i32.pow(2 - index as u32),
                _ => panic!("unrecognised character"),
            }
        }

        let seat_id = row_num * 8 + col_num;
        //println!("{} {}", line, seat_id);
        if seat_id > max_id {
            max_id = seat_id
        }

        missing_ids.retain(|&x| x != seat_id);
    }

    println!("{}", max_id);
    for missing_id in missing_ids {
        print!("{},", missing_id);
    }
    println!();

    Ok(())
}
