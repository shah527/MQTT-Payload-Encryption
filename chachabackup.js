//eyJkYXRhIjpbImN4WHU3Ym92bEo3dEZHbEY2aUpHUytpenp4RmVxaWV4Z1BVK0pVaXAiLCJCY3JFeDJpUVA3dVZFRHlCNFRpSk1pckRTM05QWnJmdyJdfQ==
let x = process.hrtime.bigint();
const { decrypt, getXchaCha20Poly1305Cipher } = require('@xchacha20-192bit/core')
let key = '14wJ5sfw+TXBHmmWk4RU9AUixM46TWxr1wqRvcenCdc='
let nonce = Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[1], 'base64')
let encr = Buffer.from(JSON.parse(Buffer.from(process.argv[2], 'base64').toString()).data[0], 'base64')
const keyBuffer = Buffer.from(key, 'base64')
const cipher = getXchaCha20Poly1305Cipher(keyBuffer)
const decr = decrypt(cipher, nonce, encr)
console.log(`decrypted text: ${Buffer.from(decr).toString()}`)
console.log((parseInt(process.hrtime.bigint()-x))/1000000)
