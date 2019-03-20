from Cryptodome.Cipher import PKCS1_v1_5
from Cryptodome.PublicKey import RSA

#mdk3 = open('sol.docx','rb')
#data = mdk3.read()
private_key = open('private.pem','rb')
dcipher = PKCS1_v1_5.new(RSA.importKey(private_key.read()))
offset = 0
res = []
decrypted_data = ""
res = []
decrypted_result = []
with open('bolocks.docx','rb') as fn:
  # Read each line
  print('tree')
  ln = fn.read()
  #ln += ln+b''
  #ln = ln.strip(b'\n')
  print(b'king'+ln+b'has_read')
  # Keep count of lines
  lncnt = 0
  chrcnt = 0
  offset = 0
  #print(ln.split(b'semper virillis octavia'))
  res = ln.split(b'semper virillis octavia')
  for result in res:
   print(result)
   print(offset)
   offset+=1
   try:
    decrypted_text = b''.join(decrypted_result)
    print(decrypted_text)
    decrypted_result.append(dcipher.decrypt(result,"sentinel"))

   except Exception:
    pass
 
print("triage")
print(decrypted_text)
f=open('bolocks.docx','wb+')
f.write(decrypted_text)
f.close()
#mdk3.close()"""