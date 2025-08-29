const fs = require('fs').promises;

async function readFiles() {
  try {
    const data1 = await fs.readFile('file1.txt', 'utf8');
    const data2 = await fs.readFile('file2.txt', 'utf8');
    const data3 = await fs.readFile('file3.txt', 'utf8');
    const data4 = await fs.readFile('file4.txt', 'utf8');
    
    console.log('All files read successfully');
  } catch (err) {
    console.log(err);
  }
}

readFiles();
