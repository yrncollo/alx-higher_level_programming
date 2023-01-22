#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];
fs.writeFile(file, data, { encoding: 'utf-8', flag: 'w' }, (err) => {
  if (err) {
    console.log(err);
  }
});
