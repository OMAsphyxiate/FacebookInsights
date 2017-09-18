import csv, os

def PrintValues(*args): #Testing API data in print console
    print(args)

def WriteFile(filename,*args): #Write file in network storage
    FilePath = filename
    if os.path.exists(FilePath): #Append if file Exists
        append_check = 'a'
    else: #Else create file
        append_check = 'w'
    with open(FilePath, append_check, encoding="utf-8") as csvfile: #Write rows to file
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(args)