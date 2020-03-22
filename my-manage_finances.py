# 計算存款占比
age = int(input('輸入年齡: '))
salary = int(input('輸入目前薪水: '))
deposit = int(input('輸入每月存款金額: '))
print('存款佔收入比例為:', deposit/salary*100, '%')
print('-----------------')

# 計算未來生活費
liv = int(input('輸入每月生活費: '))     # 每月生活費

#每年區間10年,通貨膨脹率為3%(年)
year = 0
infl = 1
liv2 = 0
liv += liv2
while year <= 50:
    age += 10
    year += 10
    infl += 0.3
    liv2 = int(liv*infl)
    print(year, '年後,我', age, '歲,每個月需要', liv2, '元才能退休' )