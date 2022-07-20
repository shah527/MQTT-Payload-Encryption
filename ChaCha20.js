let x = process.hrtime.bigint();
let crypto = require('crypto');
const decipher = crypto.createDecipheriv('chacha20', 'thirtytwobytekeyusedtotestchacha', Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64')).data[1],'base64'));
console.log(""+decipher.update(Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64')).data[0],'base64')));
console.log(process.hrtime.bigint()-x)
