import re
import csv
file = open('row.txt', 'r', encoding = "utf8")
data = file.read()
pattern1 = r'\nБИН.*(?P<bin>\b[0-9]+)'
pattern2 = r'\nНДС.*Серия.*(?P<nds>\b[0-9]+)'
t1 = re.search(pattern1, data).group("bin")
t2 = re.search(pattern2, data).group("nds")
item_pattern = r'\n(?P<name>.*)\n(?P<number>.*)\sx\s(?P<price>.*)\n(?P<sum>.*)'
item = re.compile(item_pattern)
rows = [["БИН","НДС","Наименование товара","Кол-во","Цена за единицу","Сумма"]]
for m in re.finditer(item, data):
    rows.append([t1, t2, m.group("name"), m.group("number"), m.group("price"), m.group("sum")])
with open('data.csv', 'w', newline = "", encoding = "utf8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)