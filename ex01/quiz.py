import datetime
from random import randint

mondai = ["1+0は？", "2*3は？", "9-5は？"]

kotae = [["1","１","Ⅰ","いち","イチ","一"],
["6","６","Ⅵ","ろく","ロク","六"],
["4","４","Ⅳ","よん","ヨン","四"]]

bangou = randint(0,2)

start_time = 0
fihish_time = 0

def shutudai(n):
    print(mondai[bangou])


def kaito(n):
    answer = str(input("answer="))

    for i in range(6):
        if answer == kotae[n][i]:
            print("正解！！")
            return 0
    
    print("出直してこい")
    return 0

shutudai(bangou)
start_time = datetime.datetime.now()
kaito(bangou)
fihish_time = datetime.datetime.now()
print(f"かかった時間：{(fihish_time - start_time).seconds}秒")