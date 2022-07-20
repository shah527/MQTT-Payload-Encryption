var forge = require('node-forge'); //using node-forge for decryption
//JSON array looks like this: {"data":["aPEj/0cERHFD/xaAutzuztFYDkvy+abSZyn8G/L2DrU=","QUJDREFCQ0RBQkNEQUJDRA=="]}
var inpt = JSON.parse(process.argv[2]); //reads from command line, json array with ciphertext and iv
var espMSG = inpt.data[0]; //ciphertext
var espIV = inpt.data[1]; //initialization vector
var key = 'mysecretpassword';
//var espIV = 'QUJDREFCQ0RBQkNEQUJDRA==';
//var espMSG = 'aPEj/0cERHFD/xaAutzuztFYDkvy+abSZyn8G/L2DrU=';

//base64 decode//
var iv = Buffer.from(espIV, 'base64').toString();
var cipherBuffer = Buffer.from(espMSG, 'base64');

//decryption//
var decrypt = forge.cipher.createDecipher('AES-CBC', key);
decrypt.start({ iv: iv });
decrypt.update(forge.util.createBuffer(cipherBuffer));
decrypt.finish();

console.log(decrypt.output.toString()); //returns plaintext, which is displayed in UI

