print("测试二")
year = input("猜下我的年纪:")
guess = int(year)
if guess == 24:
    print("恭喜你答对了")
else:
    if guess > 24:
        print("大了大了")
    else:
        print("小了小了")
    print("连我的年纪都不知道")
print('game over')
