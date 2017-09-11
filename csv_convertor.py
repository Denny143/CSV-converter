from bs4 import BeautifulSoup
import csv

with open("BNSF 311907.html") as fp:
    soup = BeautifulSoup(fp,"html.parser")

content = soup.find('body')

rows=[]

for row in content.find_all('div'):
   rows.append([val.text for val in row.find_all('span')])


with open('output_file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
