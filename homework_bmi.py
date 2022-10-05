def test():
    if bmi < 18.5:
        print("*" * 5, "體重過瘦", "*" * 5)
    elif 18.5 <= bmi < 24:
        print("*" * 5, "體重標準", "*" * 5)
    elif 24 <= bmi < 27:
        print("*" * 5, "體重過重", "*" * 5)
    elif 27 <= bmi < 30:
        print("*" * 5, "輕度肥胖", "*" * 5)
    elif 30 <= bmi < 35:
        print("*" * 5, "中度肥胖", "*" * 5)
    elif bmi >= 35:
        print("*" * 5, "重度肥胖", "*" * 5)
    else:
        print("檢查輸入")

height = float(input("請輸入身高(cm):"))
weight = float(input("請輸入體重(kg):"))
bmi = weight / (height / 100) ** 2
print("您的身高為:", height, "(cm)", "體重為:", weight, "(kg)")
print("BMI", "值為:", bmi)
test()

a = int(input("請輸入執行代碼:(1. 繼續, 2. 停止):"))

# while a >= 0:
#     if a == 1:
#         height = float(input("請輸入身高(cm):"))
#         weight = float(input("請輸入體重(kg):"))
#         bmi = weight / (height / 100) ** 2
#         print("您的身高為:", height, "(cm)", "體重為:", weight, "(kg)")
#         print("BMI", "值為:", bmi)
#         test()
#         a = int(input("請輸入執行代碼:(1. 繼續, 2. 停止):"))
#         continue
#     elif a == 2:
#         print("over")
#         break
#     else:
#         a = int(input("請輸入執行代碼:(1. 繼續, 2. 停止):"))
#         continue

while a >= 0:
    height = float(input("請輸入身高(cm):"))
    weight = float(input("請輸入體重(kg):"))
    bmi = weight / (height / 100) ** 2
    print("您的身高為:", height, "(cm)", "體重為:", weight, "(kg)")
    print("BMI", "值為:", bmi)
    test()
    a = int(input("請輸入執行代碼:(1. 繼續, 2. 停止):"))
    continue
    print("over")
    break
else:
    a = int(input("請輸入執行代碼:(1. 繼續, 2. 停止):"))



