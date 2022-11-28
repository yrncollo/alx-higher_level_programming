#!/usr/bin/node
const argv = parseInt(process.argv[2]);
if (!argv) console.log('Missing size');
for (let i = 0; i < argv; i++) {
  console.log('X'.repeat(argv));
}
