let x = process.hrtime.bigint();
let c = require('crypto');
let d = c.createDecipheriv('aes-128-cbc', 'mysecretpassword', Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[1], 'base64').toString());
console.log(d.update(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[0], 'base64', 'utf8'));
console.log(process.hrtime.bigint()-x)