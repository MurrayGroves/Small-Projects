use std::io;
use std::collections::VecDeque;

fn find_sub_matrix(mut matrix: Vec<VecDeque<i32>>, row_pop: usize) -> Vec<VecDeque<i32>> {
    matrix.remove(row_pop);
    for row in 0..matrix.len() {
        matrix[row].pop_front();
    }

    return matrix;
}

fn get_determinant(matrix: Vec<VecDeque<i32>>) -> i32 {
    let mut rows: Vec<i32> = Vec::new();

    for row in 0..matrix.len() {
        rows.push(matrix[row][0]);
    }

    if rows.len() == 1 {
        return rows[0];
    }

    let mut determinant: i32 = 0;
    for row in 0..rows.len() {
        let sub_matrix = find_sub_matrix(matrix.clone(), row);
        let operation = if (2 + row) % 2 == 0 { 1 } else { -1 };
        determinant = determinant + operation*get_determinant(sub_matrix)*matrix[row][0];
    }

    return determinant;
}

fn main() {
    println!("Enter matrix size:\n");
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read string");

    let size:usize = input.trim().parse().expect("Please enter a number");

    let mut matrix: Vec<VecDeque<i32>> = Vec::new();
    for row in 0..size {
        matrix.push(VecDeque::new());
        for column in 0..size {
            println!("Enter element for row {}, column {}", row+1, column+1);
            let mut element = String::new();
            io::stdin()
                .read_line(&mut element)
                .expect("Failed to read line");
            let element:i32 = element.trim().parse().expect("Please enter a number");
            matrix[row].push_back(element);
        }
    }

    for row in 0..size {
        println!("{:?}", matrix[row]);
    }
    let determinant: i32 = get_determinant(matrix);
    println!("Determinant: {:?}", determinant);
}
