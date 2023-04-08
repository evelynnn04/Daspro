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
    command=input(f'>>> ')
    if command == "help":
        help(role)
    elif command== "login":
        login(user,jumlah_baris1)
    elif command=="exit":
        Keluar=exit(Keluar)
