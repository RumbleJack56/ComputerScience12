import csv,random,sd
with open("Student Data.csv", "r+",newline="") as f:
    dataset=csv.reader(f)
    data = [x for x in dataset]
    print(data)
    for line in data:
        line += [random.choice([6,7,8,9,10,11,12]),random.choice(list("abcdef"))]
    f.seek(0,0)
    csv.writer(f,).writerows(data)