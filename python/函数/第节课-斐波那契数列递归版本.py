def fuck(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        result = fuck(n-1) * fuck(n-2)
    return result
number = int(input('请输入一个正整数：'))
result = fuck(number)
print('%d的斐波那契数列的值是%d' % (number,result))
