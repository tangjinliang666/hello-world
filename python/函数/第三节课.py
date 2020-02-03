def discount(price,rate):
    final_price = price * rate
    return final_price

old_price = float(input('请输入原价'))
rate = float(input('请输入折扣率'))
new_price = discount(old_price,rate)
print('打折后是这个价格',new_price)
