# encoding=utf-8

import csv

i=0
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        i+=1
        if i < 10:    
            print(row)
        else:
            break

def removeDuplicatedLine():
    return False
