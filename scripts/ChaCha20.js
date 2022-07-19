/*let x = process.hrtime.bigint();
const crypto = require("crypto");
//eyJkYXRhIjpbInd2OGU1S2dUYyttSWx2WDlFQldrWlRWZVQ4ZldOQWIrZ0l0dXBjQmtVUE9FIiwiYVhaMWMyVmtabTl5ZEdWemRHbHVadz09Il19
const decipher = crypto.createDecipheriv("chacha20", 'thirtytwobytekeyusedtotestchacha', Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[1], 'base64'));
console.log((decipher.update(Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[0], 'base64'))));
console.log(process.hrtime.bigint()-x)
*/
let x = process.hrtime.bigint();
let c = require('crypto');
let d = c.createDecipheriv('chacha20', 'thirtytwobytekeyusedtotestchacha', Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[1], 'base64').toString());
console.log(d.update(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[0], 'base64'));
console.log(process.hrtime.bigint()-x)