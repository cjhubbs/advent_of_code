use std::fs;

fn main() {
    let contents = fs::read_to_string("01-input.txt").expect("Cannot read file");
    let entries: Vec<&str> = contents.trim().split('\n').collect();

    let mut dial: i32 = 50;
    let mut zero_count: i32 = 0;

    for entry in entries {
        let (direction, amount) = entry.split_at(1);
        let rotations: i32 = amount.trim().parse().expect("Not a valid number.");
        let increment: i32;
        if direction == "L" {
            increment = -1;
        }
        else {
            increment = 1;
        }
        for _i in 0..rotations {
            dial += increment;
            if dial == -1 {
                dial = 99;
            }
            else if dial == 100 {
                dial = 0;
            }
            if dial == 0 {
                zero_count += 1;
            }
        }
    }
    println!("{zero_count}");
}