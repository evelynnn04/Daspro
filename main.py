from konstruktor import *
from command import *

jumlah_baris1=baris("user.csv")
jumlah_baris2=baris("candi.csv")
jumlah_baris3=baris("bahan_bangunan.csv")
user=read('user.csv',jumlah_baris1)
candi=read('candi.csv',jumlah_baris2)
bahan_bangunan=read('bahan_bangunan.csv',jumlah_baris3)

role=0
Keluar=False
while Keluar==False :
    command=input('>>> ')
    if command == "help":
        help(role)
    elif command== "login":
        if role != 0 :
            print("Login gagal!")
            print(f"Anda telah login dengan username {role}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        else :
            role=login(user,jumlah_baris1)
    elif command=="exit":
        Keluar=exit(Keluar)
    elif command=="logout":
        if role == 0 :
            print("Logout gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        else :
            role=0
            
