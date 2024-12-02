use std::{num::ParseIntError, result::Result};

fn main() {
    println!("part1: {}", part1(include_str!("input.txt")).unwrap());
    println!("part2: {}", part2(include_str!("input.txt")).unwrap());
}

fn parse_input(input: &str) -> Result<Vec<Vec<i32>>, ParseIntError> {
    input
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|num| num.parse::<i32>())
                .collect()
        })
        .collect()
}

fn part1(input: &str) -> Option<usize> {
    parse_input(input).ok()
    .map(|lines| {
        lines.into_iter().map(|line| {
            line.windows(2).map(|win| {
                win[1] - win[0]
            }).collect::<Vec<i32>>()
        }).filter(|line| {
            (line.iter().all(|&x| x >= 0) || line.iter().all(|&x| x <= 0)) && line.iter().all(|&x| x.abs() >= 1 && x.abs() <= 3)
        }).count()
    })
}


fn part2(input: &str) -> Option<usize> {
    parse_input(input).ok()
    .map(|lines| {
        lines.into_iter().filter(|line| {
            // Safety check function
            let is_safe = |line: &[i32]| {
                let diffs: Vec<i32> = line.windows(2).map(|win| win[1] - win[0]).collect();
                let all_increasing = diffs.iter().all(|&diff| diff >= 0);
                let all_decreasing = diffs.iter().all(|&diff| diff <= 0);
                let valid_differences = diffs.iter().all(|&diff| (1..=3).contains(&diff.abs()));
                (all_increasing || all_decreasing) && valid_differences
            };

            // Check if the line is already safe
            if is_safe(line) {
                return true;
            }

            // Try removing one element at a time and rechecking safety
            for i in 0..line.len() {
                let mut modified_line = line.to_vec();
                modified_line.remove(i);
                if is_safe(&modified_line) {
                    return true;
                }
            }

            false
        }).count()
    })
}



#[cfg(test)]
mod test {
use super::*;

    #[test]
    fn test1() {
        if let Some(res) = part1(include_str!("test.txt")) {
            assert_eq!(2 as usize, res)
        }
    }

    #[test]
    fn test2() {
        if let Some(res) = part2(include_str!("test.txt")) {
            assert_eq!(4 as usize, res)
        }
    }
}