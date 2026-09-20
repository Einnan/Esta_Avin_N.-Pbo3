#Python basic menggunakan csv.reader()
import csv

with open('contohCSV.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Python csv file dengan menggunkan pembatas kustom
with open('contohCSV.csv', 'r') as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:
        print(row)

#Python CSV file dengan spasi diawal
with open('contohCSV.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row)

#Python CSV files dengan tanda kutip 
with open('contohCSV.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        print(row)

#Python CSV file dengan dialek
csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

with open('kantor.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        print(row)

#Python membaca csv file dengan csv.DictReader()
with open("contohCSV.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))

#Python menggunakan class csv.Sniffer
with open('kantor.csv', 'r') as csvfile:
    sample = csvfile.read(64)
    has_header = csv.Sniffer().has_header(sample)
    print(has_header)

    deduced_dialect = csv.Sniffer().sniff(sample)

with open('kantor.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, deduced_dialect)

    for row in reader:
        print(row)