#!/usr/bin/node
const argv = parseInt(process.argv[2]);
if (argv) {
  console.log(`My number: ${argv}`);
} else {
  console.log('Not a number');
}
