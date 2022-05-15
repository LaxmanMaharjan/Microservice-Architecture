var fs = require('fs');
var rsaPemToJwk = require('rsa-pem-to-jwk');

var pem = fs.readFileSync('private_key.pem');


var jwk = rsaPemToJwk(pem, {use: 'sig'},'public');

console.log(jwk)
