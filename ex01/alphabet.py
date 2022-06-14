from random import randint
import datetime

origin_num = 10
delete_num = 2

before_alphabet = []
delete_alphabet = []
use_num = []

while len(before_alphabet) < origin_num:
    rn = randint(65,90)
    
    if rn in use_num:
        continue

    else :
        before_alphabet.append(chr(rn))

    use_num.append(rn)

after_alphabet = before_alphabet.copy()

for i in range(delete_num):
    rnum = randint(0, len(after_alphabet))
    p = after_alphabet.pop(rnum)
    delete_alphabet.append(p)

print("対象文字")
print(before_alphabet)
print("欠損文字")
print(after_alphabet)
st = datetime.datetime.now()

ans_num = int(input("欠損文字はいくつあるでしょうか？："))

check = 0

if ans_num == delete_num:
    print("正解です。それでは具体的に欠損文字を入力してください")
    for i in range(delete_num):
        ans = input(f"{i+1}文字目：")
        if ans in delete_alphabet:
            check +=1

    if check == delete_num:
        print("正解です。おめでとうございます！")
        fi = datetime.datetime.now()
        print(f"かかった時間：{(fi - st).seconds}秒")

    else :
        print("不正解です。また挑戦してください")
        fi = datetime.datetime.now()
        print(f"かかった時間：{(fi - st).seconds}秒")

else :
    print("不正解です。また挑戦してください")
    fi = datetime.datetime.now()
    print(f"かかった時間：{(fi - st).seconds}秒")