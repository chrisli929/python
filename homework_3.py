# 1.函數的練習-power
# 寫一函數power(x, n)用來計算x的n次方。
# 說明：power (5,3)即計算5^3。

# def power(x, n):
#     num = x ** n
#     print(x, "的", n, "次方為:", num)

# x = float(input("x:"))
# n = int(input("n:"))
# power(x, n)

# ------------------------------
# 2.函數的練習-is_prime
# 寫一函數is_prime(n)用來判斷n是否為質數。

# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# n = int(input("number:"))
# if is_prime(n):
#     print("質數")
# else:
#     print("不是質數")

# ------------------------------
# 3.函數的練習-prime
# 寫一函數get_prime (n)用來找出第n個質數。

# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def get_prime(n):
#     x = 1
#     y = n
#     while n > 0:
#         x += 1
#         if is_prime(x):
#             n = n - 1
#             if n == 0:
#                 print("第", y,"個質數為:", x)

# n = int(input("number:"))
# get_prime(n)

# ------------------------------
# 4.函數的練習-mersenne_prime
# 寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
# 提示：若質數滿足2^P-1=n (p為正整數)，則n為Mersenne Prime。
# 說明：當p=3時，2^3-1=7，故7為Mersenne Prime。

# def is_mersenne_prime(n):
#     imp = 2 ** n - 1
#     for i in range(2, imp):
#         if imp % i == 0:
#             return False
#     return imp

# x = 5
# num = 2
# while x > 0:
#     y = is_mersenne_prime(num)
#     if y :
#         print(y)
#         x -= 1
#         num += 1
#     else:
#         num += 1

# ------------------------------
# 5.遞迴函數的練習-factorial_recursive
# 寫一遞迴函數factorial (n)用來計算1*2*3*…*n的值。
# 提示：factorial (n) = n * factorial(n-1)，factorial(1)=1

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# n = int(input("number:"))
# ans = factorial(n)
# print(ans)

