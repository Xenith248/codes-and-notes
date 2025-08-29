const fs = require('fs')
fs.readFile('file1.txt', 'utf8', function(err, data1) {
    if (err) {
      console.log(err);
    } else {
      fs.readFile('file2.txt', 'utf8', function(err, data2) {
        if (err) {
          console.log(err);
        } else {
          fs.readFile('file3.txt', 'utf8', function(err, data3) {
            if (err) {
              console.log(err);
            } else {
              fs.readFile('file4.txt', 'utf8', function(err, data4) {
                if (err) {
                  console.log(err);
                } else {
                  // Continue with processing all data
                  console.log('All files read successfully');
                }
              });
            }
          });
        }
      });
    }
  });
  