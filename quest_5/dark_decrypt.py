#!/usr/bin/python
def reverse_bytes(byte):
 s1 = "%02x" % byte
 s2 = s1[1] + s1[0]
 return int(s2, 16)

f = open('flag.enc','rb')
data = f.read()
dec_data = [0] * 30215 
for i in range(30215/16):
 for j in range(16):
  b1 = data[16 * i + j] ^ i * i ^ j * j
  b2 = reverse_bytes(b1)
  dec_data[16 * (i + 1) - 1 - j] = b2
  
f2 = open("flag.dec", 'wb')
for i in range(30215):
 f2.write(chr(dec_data[i]))

f1.close()
f2.close() 