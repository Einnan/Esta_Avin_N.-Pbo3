#Python read csv file
import csv  

with open('contohCSV.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

#Python write csv file
with open('contohCSV2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Club", "Legend"])
    writer.writerow([1, "Barcelona", "Lionel Messi"])
    writer.writerow([2, "Manchester United", "Eric Cantona"])

#Python menggunakan pandas untuk mengendelaikan csv file
import pandas as pd
pd.read_csv("contohCSV.csv")

df = pd.DataFrame([['Sofia', 24], ['Siti nur', 22]], columns = ['Nama', 'Umur'])

df.to_csv('contohCSV.csv')