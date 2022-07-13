//time taken ~17ms
let c = require('crypto'); //changed libraries for efficiency
let d = c.createDecipheriv('aes-128-cbc', 'mysecretpassword', Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[1], 'base64').toString());
console.log(d.update(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[0], 'base64', 'utf8') + d.final('utf8'));
