#!/usr/bin/node
const argv = parseInt(process.argv[2]);
let i = 0;
if (!argv) console.log('Missing number of ocurrences');
while (i < argv) {
  console.log('C is fun');
  i++;
}
