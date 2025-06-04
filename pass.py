import random

chars= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passcode=""
pertanyaan= int(input("Masukan jumlah passcode yang ingin anda buat:"))

for i in range(pertanyaan):
    passcode+=random.choice(chars) 
    
print("Passcode yang terbuat adalah", passcode)
