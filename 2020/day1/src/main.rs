use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() -> std::io::Result<()> {
    let input_file = File::open("input.txt")?;
    let reader = BufReader::new(input_file);
    let lines = reader.lines().map(|l| l.unwrap().parse::<i32>().unwrap()).collect::<Vec<i32>>();


    for (index1, line1) in lines.iter().enumerate() {
        for (index2, line2) in lines.iter().enumerate() {
            if index1 <= index2 {
                continue;
            }
            let sum = line1 + line2;
            if sum == 2020 {
                let product = line1 * line2;
                println!("{}", product);
            }
            
        }
    }

    for (index1, line1) in lines.iter().enumerate() {
        for (index2, line2) in lines.iter().enumerate() {
            for (index3, line3) in lines.iter().enumerate() {
                if (index1 <= index2) || (index2 <= index3) || (index1 <= index3) {
                    continue;
                }
                let sum = line1 + line2 + line3;
                if sum == 2020 {
                    let product = line1 * line2 * line3;
                    println!("{}", product);
                }
            }
        }
    }

    Ok(())
}