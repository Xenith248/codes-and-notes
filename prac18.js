const fs = require('fs').promises;

async function readFiles() {
  try {
    // Read file1.txt
    const data1 = await fs.readFile('file1.txt', 'utf8');
    console.log('File 1 read:', data1);

    // Read file2.txt
    const data2 = await fs.readFile('file2.txt', 'utf8');
    console.log('File 2 read:', data2);

    // Read file3.txt
    const data3 = await fs.readFile('file3.txt', 'utf8');
    console.log('File 3 read:', data3);

    // Read file4.txt
    const data4 = await fs.readFile('file4.txt', 'utf8');
    console.log('File 4 read:', data4);

    console.log('All files read successfully');
  } catch (err) {
    // Catch any error that occurs in any of the file reads
    console.log('Error reading files:', err);
  }
}

readFiles();
