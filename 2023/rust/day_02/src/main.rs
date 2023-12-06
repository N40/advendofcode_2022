use std::fs;
use regex::Regex;
use std::cmp::max;

fn read_lines(filename: &str) -> Vec<String>
{
    fs::read_to_string(filename)
        .unwrap()  // panic on possible file-reading errors
        .lines()  // split the string into an iterator of string slices
        .map(String::from)  // make each slice into a string
        .collect()  // gather them together into a vector
}


#[derive(Debug)]
struct Game {
    id: usize,
    draws: Vec<[usize; 3]>,
}

fn read_input(filename: &str) -> Vec<Game> {
    let lines = read_lines(&filename);
    let mut games: Vec<Game> = Vec::new();
    let re_game = Regex::new(r"(\d+)").unwrap();
    let re_red = Regex::new(r"(\d+) red").unwrap();
    let re_green = Regex::new(r"(\d+) green").unwrap();
    let re_blue = Regex::new(r"(\d+) blue").unwrap();
    //   Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue

    for line in lines {
        let main_parts = line.split(":").collect::<Vec<&str>>();
        let mut game: Game = Game { id: 0, draws: [].to_vec() };
        game.id = re_game.find(main_parts[0]).unwrap().as_str().parse::<usize>().unwrap();
        for part in main_parts[1].split(";").collect::<Vec<&str>>()
        {
            game.draws.push([0, 0, 0]);
            if let Some(match_red) = re_red.captures(part) {
                game.draws.last_mut().unwrap()[0] = match_red.get(1).unwrap().as_str().parse::<usize>().unwrap();
            }
            if let Some(match_red) = re_green.captures(part) {
                game.draws.last_mut().unwrap()[1] = match_red.get(1).unwrap().as_str().parse::<usize>().unwrap();
            }
            if let Some(match_red) = re_blue.captures(part) {
                game.draws.last_mut().unwrap()[2] = match_red.get(1).unwrap().as_str().parse::<usize>().unwrap();
            }
        }
        println!("{0:?}", game);

        games.push(game);
    }

    games
}


fn main() {
    let limits: [usize; 3] = [12, 13, 14];

    let games = read_input("input.txt");
    let mut count: usize = 0;
    let mut count_2: usize = 0;

    for game in games {
        let mut mins: [usize; 3] = [0, 0, 0];
        let mut valid: bool = true;
        for draw in game.draws
        {
            for i in 0..3 {
                if draw[i] > limits[i] { valid = false; }

                mins[i] = max(mins[i], draw[i]);
            }
        }

        if valid { count += game.id }

        count_2 += mins[0] * mins[1] * mins[2]
    }

    println!("{count:?},");
    println!("{count_2:?},");
}