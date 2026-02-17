import csv
headers = ["isim","soyisim"]
data = {"isim": "zeynep" , "soyisim": "demir"}
with open("kullanicim.csv", "w" , encoding = "utf-8") as file:
    csv_writer = csv.DictWriter(file, fieldnames= headers)
    csv_writer.writerow(data)