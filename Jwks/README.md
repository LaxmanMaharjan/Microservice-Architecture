# Converting .pem file to jwks

## Important links
- [node-jose](https://www.npmjs.com/package/node-jose)
- [node-jose Example](https://www.jvt.me/posts/2019/01/10/x509-pkcs8-pem-key-to-jwks-node/) 
- [rsa-pem-to-jwk](https://www.npmjs.com/package/rsa-pem-to-jwk) 


### node-jose
When working with public/private keypairs, it's most likely you'll be dealing with files most commonly ending in .pem (X.509 certificates). However, there are cases where you'll want to convert your traditionally formatted file to a JWKS format.
Use node-jose for this.

