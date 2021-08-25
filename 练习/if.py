# 测试 if 条件判断的使用

cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


# 条件判断
car = "bmw"
print(car == "bmw")

car = "audi"
print(car == "bmw")

# 检查是否忽略大小写
car = "Audi"
print(car == "audi")


# 转换为小写再进行判断
car = "Audi"
print(car.lower() == "audi")
print(car)      # 不会修改原本的值

# 检查是否不相等
food = "mushrooms"
if food != "anchovies":
    print("持有小银鱼")


# 检查两个数是否不等
age = 17
if age != 42:
    print("那不是正确答案，请再试一次！")


# 各种数学比较
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)


# 使用and检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)


# 使用or检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)


# 检查特定值是否包含在列表中
packaging = ["火腿", "面粉", "孜然"]
print("孜然" in packaging)
print("洋葱" in packaging)


# 检查特定值是否不包含在列表中
users = ["Tang", "Zhan", "Hao"]
user = "Tao"
if user not in users:
    print(f"{user.title()}如果你愿意，你可以发表一个回复")     # 如果不包含则执行判断语句


# 练习
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


a = "Tang"
b = "tang"
print(a == b)
print(a.lower() == b)

age = 18
print(age > 21)     # 大于
print(age >= 21)     # 大于等于
print(age < 21)     # 小于
print(age <= 21)     # 小于等于
print(age == 21)     # 等于
print(age != 21)     # 不等于


# if-elif-else
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"你需要支付{price}元")

# 多个elif代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"你需要支付{price}元")


# 省略else代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"你需要支付{price}元")


# 多个条件满足时使用多个if判断
ingredients = ["孜然粉", "辣椒粉", "胡椒粉"]
if "辣椒油" in ingredients:
    print("添加辣椒油")
if "孜然粉" in ingredients:
    print("添加孜然粉")
if "胡椒粉" in ingredients:
    print("多添加胡椒粉")
print("\n完成你的披萨")


# 练习
alien_color = ["green", "yellow", "red"]
if "green" in alien_color:
    print("恭喜你获得了5分")

alien_color = ["green", "yellow", "red"]
if "green" in alien_color:
    print("您因射杀了外星人获得了5分")
else:
    print("恭喜你获得了10分")


alien_color = ["green", "yellow", "red"]
if "green" in alien_color:
    print("恭喜你获得了5分")
elif "yellow" in alien_color:
    print("恭喜你获得了10分")
else:
    print("恭喜你获得了15分")

# 人声的阶段
age = 20
if age < 2:
    life = "婴儿"
elif age < 4:
    life = "幼儿"
elif age < 13:
    life = "儿童"
elif age < 20:
    life = "青少年"
elif age < 65:
    life = "成年人"
else:
    life = "老年人"
print(f"您是{life}")


# 喜欢的水果
favorite_fruits = ["香蕉", "苹果", "火龙果"]
if "梨子" in favorite_fruits:
    print("我喜欢梨子")
if "香蕉" in favorite_fruits:
    print("我喜欢香蕉")
if "桃子" in favorite_fruits:
    print("我喜欢桃子")
if "火龙果" in favorite_fruits:
    print("我喜欢火龙果")
if "山竹" in favorite_fruits:
    print("我喜欢山竹")
print("这就是我喜欢的水果")


