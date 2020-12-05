use std::fs;
use regex::Regex;
use std::collections::HashMap;

fn validate_year(year: &str, min: i32, max: i32) -> bool {
    let re = Regex::new(r"^\d{4}$").unwrap();
    let mat = re.find(year);
    match mat {
        None => false,
        Some(m) => {
            let year = m.as_str().parse::<i32>().unwrap();
            (year >= min) && (year <= max)
        },
    }
}

fn main() -> std::io::Result<()> {
    // let required_fields: [&str; 8] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"];
    let required_fields: [&str; 7] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
    

    let passports_raw = fs::read_to_string("input.txt")?;
    let passports = passports_raw.split("\n\n").map(|s| s.replace("\n", " "));

    let mut total_part1 = 0;
    let mut total_part2 = 0;
    for passport in passports {
        //println!("{}", passport);
        //println!("checking passport no. {}", passport_index);
        // start by assuming valid
        total_part1 += 1;
        total_part2 += 1;
        let mut passport_dict = HashMap::new();
        for entry in passport.split(" ") {
            let entry_split: Vec<&str> = entry.split(":").collect();
            let field = entry_split[0];
            let value = entry_split[1];
            passport_dict.insert(field, value);
        }
        for required_field in required_fields.iter() {
            //println!("checking field {} of passport {}", required_field, passport_index);
            // if invalid decrement and go to next passport
            if !passport_dict.contains_key(required_field) {
                //println!("passport no. {} doesn't contain {}", passport_index+1, required_field);
                total_part1 -= 1;
                total_part2 -= 1;
                break
            }
            let value = passport_dict.get(required_field).unwrap();
            // if required field exists, check if value is valid
            let result: bool = match *required_field {
                "byr" => validate_year(value, 1920, 2002),
                "iyr" => validate_year(value, 2010, 2020),
                "eyr" => validate_year(value, 2020, 2030),
                "hgt" => {
                    let re = Regex::new(r"^(?P<num>\d{2}\d?)(?P<unit>cm|in)$").unwrap();
                    let caps = re.captures(value);
                    match caps {
                        None => false,
                        Some(c) => {
                            match c.name("unit").unwrap().as_str() {
                                "cm" => {
                                    let num_str = c.name("num").unwrap().as_str();
                                    if num_str.len() != 3 {
                                        false
                                    } else {
                                        let num = num_str.parse::<i32>().unwrap();
                                        (num >= 150) && (num <= 193)
                                    }
                                },
                                "in" => {
                                    let num_str = c.name("num").unwrap().as_str();
                                    if num_str.len() != 2 {
                                        false
                                    } else {
                                        let num = num_str.parse::<i32>().unwrap();
                                        (num >= 59) && (num <= 76)
                                    }
                                },
                                _ => panic!("unrecognised unit")
                            }
                        },
                    }
                },
                "hcl" => {
                    let re = Regex::new(r"^#[0-9a-f]{6}$").unwrap();
                    re.is_match(value)
                },
                "ecl" => {
                    let re = Regex::new(r"^(?:amb|blu|brn|gry|grn|hzl|oth)$").unwrap();
                    re.is_match(value)
                },
                "pid" => {
                    let re = Regex::new(r"^\d{9}$").unwrap();
                    re.is_match(value)
                },
                "cid" => {
                    // ignored
                    true
                }
                _ => panic!("unrecognised field"),
            };
            if !result {
                total_part2 -= 1;
                break
            }
        }
    }

    println!("{}", total_part1);
    println!("{}", total_part2);

    Ok(())
}