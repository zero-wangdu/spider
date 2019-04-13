import csv

read_file = open('asiavideo.csv', 'r', encoding='gb18030')
save_file = open('asia_url.csv', 'w', newline='', encoding='gb18030')

file = csv.reader(read_file)

writer = csv.writer(save_file)
for i in file:
    li = eval(i[2])
    print(li)
    temp = [i[0], i[1], li[0], li[1]]
    print(temp)
    writer.writerow(temp)

read_file.close()
save_file.close()

