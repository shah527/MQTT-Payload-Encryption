//eyJkYXRhIjpbImN4WHU3Ym92bEo3dEZHbEY2aUpHUytpenp4RmVxaWV4Z1BVK0pVaXAiLCJCY3JFeDJpUVA3dVZFRHlCNFRpSk1pckRTM05QWnJmdyJdfQ==
let x = process.hrtime.bigint();
const { decrypt, getXchaCha20Poly1305Cipher } = require('@xchacha20-192bit/core')
console.log(Buffer.from(decrypt(getXchaCha20Poly1305Cipher(Buffer.from('14wJ5sfw+TXBHmmWk4RU9AUixM46TWxr1wqRvcenCdc=', 'base64')), Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[1], 'base64'), Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[0], 'base64'))).toString())
console.log(process.hrtime.bigint()-x)
