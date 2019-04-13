import os
import csv

def getNameDic():
    f = open('all-mv-url-2.csv', 'r', encoding='gb18030')
    file = csv.reader(f)
    video_dic = {}
    for i in file:
        ename = i[2].split('/')[-1]
        suffix = ename.split('.')[-1]
        cname = i[1][:-1] + '.' + suffix
        video_dic[ename] = cname

    print(video_dic)
    return video_dic

video_dic = getNameDic()

def start():
    abs_path = os.getcwd()
    file_li = os.listdir(abs_path)
    for f in file_li:
        temp = video_dic.get(f)
        if temp:
            os.rename(f, temp)

start()

