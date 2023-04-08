def length (list):
    list_temp=append(list,"%")
    j=0
    while list_temp[j]!="%":
        j+=1

    return j

def merge(list):
    array=''
    for i in range (length(list)):
        array+=list[i]    
    return [array]

def init(list):
    if list and list[:-1]:
        return list[:-1]
    else:
        return []
 
def append(list1,list2):
    list=[*list1,*list2]

    return list

def baris(file_csv):
    with open(file_csv) as csv:
        jumlah_baris = 0
        for i in csv:
            jumlah_baris += 1
    return jumlah_baris

def read(file_csv,jumlah_baris):
    with open(file_csv) as csv:
        baris=''
        rows_temp=[]
        count=0
        for i in range (jumlah_baris):
            baris=f'{next(csv)}'
            rows_temp=append(rows_temp,[baris])
            count+=1
        rows=[]    
        for j in range (count):
            temp=[]
            for huruf in rows_temp[j]:
                if huruf != '\n' :
                    temp=append(temp,[huruf])
            array=temp[0]
            for k in range (1,length(list(temp))):
                array+=temp[k]
            rows=append(rows,[array])

        return rows
    
def user_part(user,jumlah_baris):
    list_user=[]
    list_pass=[]
    list_role=[]
    for i in range(jumlah_baris):
        arr_user=[]
        temp_user=[]

        arr_pass=[]
        temp_pass=[]

        arr_role=[]
        temp_role=[]

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
        while j<length(list(user[i])):
            kata_role=list(user[i])
            arr_role+=kata_role[j]
            j+=1
        temp_user=merge(arr_user)
        temp_pass=merge(arr_pass)
        temp_role=merge(arr_role)
        list_user=append(list_user,temp_user)
        list_pass=append(list_pass,temp_pass)
        list_role=append(list_role,temp_role)

    return (list_user,list_pass,list_role)