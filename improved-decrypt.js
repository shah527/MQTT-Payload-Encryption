//faster runtime (~47ms ryzen 7 5800h, 16gb ram, windows 11, background processes running)

let f = require('node-forge');
let d = f.cipher.createDecipher('AES-CBC', 'mysecretpassword');
d.start({ iv: Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[1], 'base64').toString() });
d.update(f.util.createBuffer(Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[0], 'base64')));
d.finish();
console.log(d.output.toString());
