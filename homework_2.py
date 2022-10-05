# 1.
# 迴圏的練習 - factor
# 輸入一正整數，求其所有的因數。
# 說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36,
#
# number = int(input("number:"))
# print("因數為:", end="\t")
# for i in range(1, number+1):
#     if number % i == 0:
#         print(i, end=",")

#--------------------------------
# 2.
# 迴圏的練習 - perfect_number
# 一個數字若等於其所有因數的總和，則此數為perfect number。
# 找出100以內所有的完美數。
# 說明：6
# 的因數為1, 2, 3，6 = 1 + 2 + 3，故6為完美數。

# for i in range(1, 100+1):
#     a = 0
#     for j in range(1, i+1):
#         if i % j == 0 and i != j:
#             a += j
#     if a == i:
#         print(a)

#--------------------------------
# 3.
# 迴圏的練習 - amstrong
# Amstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。
# 找出所有的Amstrong數。
# 說明：153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3，故153為Amstrong數。
# (2 ^ 3 表示 2 的 3 次方, 3 ^ 3 表示 3 的 3 次方)

# for i in range(100, 999+1):
#     x = (i // 100) ** 3
#     y = ((i - (i // 100 * 100)) // 10) ** 3
#     z = (i - (i // 100 * 100) - (i - (i // 100 * 100)) // 10 * 10) ** 3
#     if x + y + z == i:
#         print(i)

#-------------------------------
# 4.
# 迴圈的練習 - prime
#
# 輸入一正整數，找出所有小於或等於的質數。

# number = int(input("number:"))
# print(number, "的質數為:", end="\t")
# for i in range(2, number+1):
#     for j in range(2, i):
#         if i % j == 0 and i != j:
#             break
#     else:
#         print(i, end=",")

# 5.
# 迴圈敘述的練習 - interest
# 某人A以10 % 單利投資100000元，某人B則以5 % 複利投資100000元。
# 計算多少年後某人B的投資可以超過某人A，並將此時兩人錢數印出。(27年後)
# 提示：單利公式：P(1 + r * n)
# 複利公式：P(1 + r) ^ n
# P：本金，r：利率，n：多少年
# (備註︰(1+r) ^ n
# 表示(1 + r)的n次方)

# year = 1
# while True:
#     A = 100000 * (1 + (0.1 * year))
#     B = 100000 * (1 + 0.05) ** year
#     if A > B:
#         year = year + 1
#     else:
#         print("第", year, "年")
#         print("A:", A, "元")
#         print("B:", B, "元")
#         break




