use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() -> std::io::Result<()> {
    let input_file = File::open("input.txt")?;
    let reader = BufReader::new(input_file);
    let lines = reader.lines();

    let     angles: [(i32, i32); 5] = [(1,1), (3,1), (5,1), (7,1), (1,2)];
    let mut totals: [i32       ; 5] = [0    , 0    , 0    , 0    , 0    ];

    let map: Vec<Vec<char>> = lines.map(|l| l.unwrap().chars().collect()).collect();

    for (index, angle) in angles.iter().enumerate() {
        for (y, line) in map.iter().enumerate() {
            let y = y as i32;
            // we don't need to worry about this line if it isn't a multiple of the y step of angle
            if y % angle.1 != 0 {
                continue;
            }
            let step = y / angle.1;

            // the toboggan's x position at this step
            let position = (step * angle.0) % line.len() as i32;

            for (x, character) in line.iter().enumerate() {
                let x = x as i32;
                if x == position && *character == '#' {
                    totals[index] += 1;
                }
            }
        }   
    }

    println!("{}", totals[1]);
    println!("{}", totals.iter().product::<i32>());

    Ok(())
}