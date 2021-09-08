use std::io;

fn find_sub_matrix(matrix: Vec<Vec<i32>>, row: usize) -> Vec<Vec<i32>> {

}

fn determinant(matrix: Vec<Vec<i32>>) -> i32 {
    let mut dets: Vec<i32> = Vec::new();
    let mut rows: Vec<i32> = Vec::new();

    for row in matrix.len() {
        rows.push(row[0]);
    }
    println!("{:?}", rows);

    if rows.len() == 1 {
        return rows[0];
    }

    for row in 0..rows.len() {
        let sub_matrix = find_sub_matrix(matrix.copy(), row);
        dets.push(determinant(sub_matrix));
    }

    return 1;
}

fn main() {
    println!("Enter matrix size:\n");
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read string");

    let size:usize = input.trim().parse().expect("Please enter a number");

    let mut matrix: Vec<Vec<i32>> = Vec::new();
    for row in 0..size {
        matrix.push(Vec::new());
        for column in (0..size).rev(){
            let mut element = String::new();
            io::stdin()
                .read_line(&mut element)
                .expect("Failed to read line");
            let element:i32 = element.trim().parse().expect("Please enter a number");
            matrix[row].push(element);
        }
    }

    println!("{:?}", matrix)

}
