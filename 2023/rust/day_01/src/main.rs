use std::fs;
use std::collections::HashMap;
use std::collections::BTreeMap;


fn read_lines(filename: &str) -> Vec<String> {
    fs::read_to_string(filename)
        .unwrap()  // panic on possible file-reading errors
        .lines()  // split the string into an iterator of string slices
        .map(String::from)  // make each slice into a string
        .collect()  // gather them together into a vector
}

fn main() {
    let lines = read_lines("input.txt");

    let mut c = 0;

    let mut dict = HashMap::<String, i32>::from([
        // Part 2 compability
        (String::from("zero"), 0),
        (String::from("one"), 1),
        (String::from("two"), 2),
        (String::from("three"), 3),
        (String::from("four"), 4),
        (String::from("five"), 5),
        (String::from("six"), 6),
        (String::from("seven"), 7),
        (String::from("eight"), 8),
        (String::from("nine"), 9),
        //
    ]);
    for n in 0..10 {
        dict.insert(n.to_string(), n);
    }


    for line in lines {
        let mut chars: BTreeMap<usize, i32> = BTreeMap::new();

        for (s, v) in &dict
        {
            let f = line.find(&*s);
            if f.is_some()
            {
                chars.insert(f.unwrap(), *v);
            }
            let f = line.rfind(&*s);
            if f.is_some()
            {
                chars.insert(f.unwrap(), *v);
            }
        }


        let i1: i32 = *chars.first_key_value().unwrap().1;
        let i2: i32 = *chars.last_key_value().unwrap().1;


        let mut new_string = String::from("");

        new_string += &i1.to_string();
        new_string += &i2.to_string();


        let n: i32 = new_string.parse().unwrap();
        println!("{n:?}", );

        c += n;
    }

    println!("\n{c:?}", );
}