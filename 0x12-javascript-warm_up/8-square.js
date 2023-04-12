#!/usr/bin/node
if (!process.argv[2] || !parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  for (let i = 1; i <= size; i++) {
    let row = '';
    for (let j = 1; j <= size; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
