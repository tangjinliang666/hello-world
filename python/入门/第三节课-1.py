bingo= "大帅哥"
answer = input("请输入夸我的一句话：")

while True:
    if answer == bingo:
        break
    answer = input("不是我想听的那句，回答上来才能退出去")

print("听的我真舒服，你可以走了")
