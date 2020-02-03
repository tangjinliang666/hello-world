print("测试三")
year = input("猜下我的年纪:")
guess = int(year)
while  guess != 24:
    if guess > 24:
        print("大了大了")
        print("连我的年纪都不知道")
    if guess < 24:
        print("小了小了")
        print("连我的年纪都不知道")
    year = input ("再给你一次机会")
    guess = int(year)
if guess == 24:
    print("恭喜你答对了")
print('game over')
