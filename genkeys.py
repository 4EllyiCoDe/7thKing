from Cryptodome.Cipher import PKCS1_v1_5
from Cryptodome.PublicKey import RSA

key = RSA.generate(1024)

#Write keys to respective files
public_key = open('public.pem','wb')
public_key.write(key.publickey().exportKey('DER'))
private_key = open('private.pem','wb')
private_key.write(key.exportKey('DER'))
public_key.close()
private_key.close()

#Read keys
public_key = open('public.pem','rb')
private_key = open('private.pem','rb')
cipher = PKCS1_v1_5.new(RSA.importKey(public_key.read()))
dcipher = PKCS1_v1_5.new(RSA.importKey(private_key.read()))
data=cipher.encrypt(b'Yes I\'m the God of hacking')
print(data)
print(dcipher.decrypt(data,"sentinel"))
print("Public key %s"%public_key.read())
print("Private key %s"%private_key.read())
public_key.close()
private_key.close()