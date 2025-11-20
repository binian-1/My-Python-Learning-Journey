# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

# 生成1-100的随机数字
target_number = random.randint(1, 100)
guess_count = 0

# 游戏开始提示语
print("你好，我是小P！\n我已经生成了一个1-100的数字，请开始猜测吧！")

# 猜数游戏过程
while True:
    try:
        user_guess = int(input("请输入你猜测的数字: "))
        guess_count += 1
        
        # 判断猜测结果
        if user_guess < target_number:
            print("猜小了，再试试！")
        elif user_guess > target_number:
            print("猜大了，再试试！")
        else:
            
            # 结果评价
            if guess_count == 1:
                print("你真是神机妙算！一次就猜到了！正确答案是:", {target_number})
            elif guess_count <= 6:
                print("太厉害了吧！才",guess_count,"次就猜到了！正确答案是:" , {target_number})
            else:
                print("恭喜你！正确答案是:",{target_number})
                print("你总共猜了",guess_count,"次。")
            break  # 猜对后直接退出游戏
                
    except ValueError: # 输入错误提示
        print("输入无效，请输入一个整数！")

# 游戏结束提示语
print("\n游戏结束，谢谢参与！欢迎再来找小P玩！")