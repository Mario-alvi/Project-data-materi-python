import os
import random
import string
print(f"{' Data Film':±^40}")
data = dict()
while True:

    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range (3))
    print(f"keyfinal = {keyFinal}")
    Namafilm = input("Enter Nama film\t\t:")
    Tahun= input("Enter Tahun\t\t:")
    sutradara = input("Enter sutradara\t\t:")
    data[ keyFinal ] =  { ' Namafilmkey ' : Namafilm,'tahunkey' : Tahun,'sutradarakey' : sutradara  }
    opsi = input("ingin input data LAGI GAK(Y/T)").lower()
    if opsi == 't':
        break

print("-"*40)
print(f"Key\t Nama film\t tahun\t sutradara")
print("-"*40)

for key, value in data.items():
    print(f"{key}.\t{ data [key][' Namafilmkey ']}\t {data[key]['tahunkey']}\t {data[key]['sutradarakey']}")
