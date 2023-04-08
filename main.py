from konstruktor import *

jumlah_baris1=baris("user.csv")
jumlah_baris2=baris("candi.csv")
jumlah_baris3=baris("bahan_bangunan.csv")
user=read('user.csv',jumlah_baris1)
candi=read('candi.csv',jumlah_baris2)
bahan_bangunan=read('bahan_bangunan.csv',jumlah_baris3)

def login(user,jumlah_baris):
    Username=input("Username : ")
    Password=input("Password : ")
    list_user=[]
    list_pass=[]
    for i in range(jumlah_baris):
        arr_user=[]
        temp_user=[]
        arr_pass=[]
        temp_pass=[]
        count=0
        j=0
        while count<1:
            kata_user=list(user[i])
            if kata_user[j] == ';':
                count+=1
                j+=1
            else:
                arr_user+=kata_user[j]
                j+=1
        while 0<count<2:
            kata_pass=list(user[i])
            if kata_pass[j] == ';':
                count+=1
                j+=1
            else:
                arr_pass+=kata_pass[j]
                j+=1
        temp_user=merge(arr_user)
        temp_pass=merge(arr_pass)
        list_user=append(list_user,temp_user)
        list_pass=append(list_pass,temp_pass)
    
    user_valid=False
    pass_valid=False
    for i in range (length(list_user)):
        if Username == list_user[i] :
            user_valid=True
            if Password==list_pass[i]:
                pass_valid=True
                break
    
    if user_valid==True and pass_valid==True:
        return (f'\nSelamat datang, {Username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')
    elif user_valid==True and pass_valid==False:
        return("\nPassword salah!")
    else:
        return("\nUsername tidak terdaftar!")
                    

print(login(user,jumlah_baris1))


