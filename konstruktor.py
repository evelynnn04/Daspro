def length (list):
    i=0
    while init(list)!=[]:
        i+=1
        list=init(list)
    return i+1

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
    list=list1+list2
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
    

