#Nama   : Arya Yudhistira
#NIM    : 121140115
coba=0
while coba <3:
    user=input("Username anda : ")
    password=input("Password anda : ")
    if user=="informatika" and password=="12345678":
        print("Berhasil login!")
        break
    else:
        print("Username atau password salah coba lagi")
        coba+=1
if coba >=3:
    print("Maaf, akun anda telah diblokir!")
