import os
import csv
import pyodbc

# TEXT FILE CLEAN
#with open('C:\Path\To\Raw.csv', 'r') as reader, open('C:\Path\To\Clean.csv', 'w') as writer:
with open('D:\타사B migration test\새파일.csv', 'w') as writer:
    write_csv = csv.writer(writer, lineterminator='\n')

    for line in read_csv:
        if len(line[1]) > 0:
            write_csv.writerow(line)

# DATABASE CONNECTION
access_path = "C:\Path\To\Access\\DB.mdb"
con = pyodbc.connect("DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={};" \
                     .format(access_path))

# RUN QUERY
strSQL = "SELECT * INTO [TableName] FROM [text;HDR=Yes;FMT=Delimited(,);" + \
         "Database=C:\Path\To\Folder].Clean.csv;"
cur = con.cursor()
cur.execute(strSQL)
con.commit()

con.close()                            # CLOSE CONNECTION
os.remove('C\Path\To\Clean.csv')       # DELETE CLEAN TEMP

'''
files=`find ./ -name *.accdb -o -name *.mdb`
while read -r filename; do
    echo "CONVERTING FILE $filename"
    _basedir=`pwd`
    _basename="${filename%.*}"
    mkdir -p "$_basename"
    cd "$_basename"
    python3 ~/software/access2csv.py  "$_basedir/$filename" 
    cd "$_basedir"
    echo "REMOVE FILE $filename"
    rm "$filename"
    '''