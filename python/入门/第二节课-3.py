print("测试四")
jishu = 1
year = input("猜下我的年纪:")
guess = int(year)
while  guess != 24 and jishu !=3:
    if guess > 24:
        print("大了大了")
        print("连我的年纪都不知道")
    if guess < 24:
        print("小了小了")
        print("连我的年纪都不知道")
    year = input ("再给你一次机会")
    guess = int(year)
    jishu = jishu + 1 
if guess == 24:
    print("恭喜你答对了")
if jishu == 3:
    print("给你3次机会都不知道，真没用")
print('game over')
