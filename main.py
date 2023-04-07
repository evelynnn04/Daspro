def baris(file_csv):
    with open(file_csv, 'r') as csv:
        baris = 0
        for i in csv:
            baris += 1
    return baris - 1


def load_csv(file_csv,lines):
    with open(file_csv, 'r') as csv:
        line=f'{next(csv)}'
        waw=''
        for i in range (lines-1):
            waw=f'{next(csv)}'
            print(waw)
        rows=[]
        for i in line:
            if i != '\n' :
                rows.append(i)
        array=rows[0]
        for j in range (1,len(rows)):
            array+=rows[j]
        return [array]

jumlah_baris=baris("user.csv")
data=load_csv('user.csv',jumlah_baris)

print(data)


def add_to_csv(file_csv, data):
    # Get the header row from the first dictionary in the data list
    header = list(data[0].keys())
    # Open the CSV file_csv for appending
    with open(file_csv, 'a') as csvfile_csv:
        # Write the header row to the file_csv if it doesn't exist already
        file_csv_empty = csvfile_csv.tell() == 0
        if file_csv_empty:
            csvfile_csv.write(','.join(header) + '\n')
        # Write each row to the file_csv
        for row in data:
            values = []
            for col_name in header:
                values.append(str(row[col_name]))
            csvfile_csv.write(','.join(values) + '\n')
