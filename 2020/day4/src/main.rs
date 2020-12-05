use regex::Regex;
use std::collections::HashMap;
use std::fs;

fn re_match(s: &str, re: &str) -> bool {
    Regex::new(re).unwrap().is_match(s)
}

fn validate_year(year: &str, min: i32, max: i32) -> bool {
    re_match(year, r"^\d{4}$") && (min..max + 1).contains(&year.parse().unwrap())
}

fn validate_height(height: &str) -> bool {
    re_match(height, r"^\d{2,3}(cm|in)$") && {
        let split_index = height.len() - 2;
        match &height[split_index..] {
            "cm" => 150..193 + 1,
            _ => 59..76 + 1,
        }
        .contains(&(&height[..split_index]).parse::<i32>().unwrap())
    }
}

fn main() -> std::io::Result<()> {
    let required_fields: [&str; 7] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

    let mut validators: HashMap<&str, fn(&str) -> bool> = HashMap::new();
    validators.insert("byr", |v| validate_year(v, 1920, 2002));
    validators.insert("iyr", |v| validate_year(v, 2010, 2020));
    validators.insert("eyr", |v| validate_year(v, 2020, 2030));
    validators.insert("hgt", validate_height);
    validators.insert("hcl", |v| re_match(v, r"^#[0-9a-f]{6}$"));
    validators.insert("ecl", |v| re_match(v, r"^amb|blu|brn|gry|grn|hzl|oth$"));
    validators.insert("pid", |v| re_match(v, r"^\d{9}$"));
    validators.insert("cid", |_| true);

    let _passports = fs::read_to_string("input.txt")?;
    let passports = _passports.split("\n\n").map(|s| s.replace("\n", " "));

    let mut total_part1 = 0;
    let mut total_part2 = 0;
    for passport in passports {
        let mut all_required_fields_present = true;
        let mut all_required_fields_valid = true;

        let passport_dict: HashMap<&str, &str> = passport
            .trim()
            .split(" ")
            .map(|s| (&s[..3], &s[4..]))
            .collect();

        for required_field in required_fields.iter() {
            if !passport_dict.contains_key(required_field) {
                all_required_fields_present = false;
                break;
            }

            let validator = validators.get(required_field).unwrap();
            let value = passport_dict.get(required_field).unwrap();
            if !validator(value) {
                all_required_fields_valid = false;
            }
        }

        if all_required_fields_present {
            total_part1 += 1;
            if all_required_fields_valid {
                total_part2 += 1;
            }
        }
    }

    println!("{}", total_part1);
    println!("{}", total_part2);

    Ok(())
}
