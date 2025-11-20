# My-Python-Learning-Journey
- 以下我Python课程的代码记录 欢迎大家根据代码文件中的题目要求设计代码并与我交流。
- 更新时间：2025/11/20
- 更新人：binian

## 代码列表
### 1. 深圳大学课程成绩计算器 (题目1.py)
这是一个专为深圳大学学生设计的成绩计算工具。它可以根据您当前的平时分和课程成绩占比，快速计算出为了达到目标等级，期末考需要考多少分。  
#### 功能特点：​​  
- 输入课程信息​：输入课程名称、平时分和期末考的占比。  
- 参照深大标准​：使用深圳大学通用的等级分数对照表（A+, A, B+, B, C+, C, D, F）。  
- 智能计算​：自动计算出达到目标等级所需的期末分数范围。  
- 情景分析​：会判断是否已经达成目标或是否无法达成目标，并给出相应的鼓励信息。  
#### 运行方法：​​
- 下载 *题目1.py* 代码（或复制粘贴代码示例部分代码）。
- 确保您的电脑已安装 Python（建议使用 Python 3.x）。
- 导航到存放 *题目1.py* 文件的目录。
- 打开并根据程序的提示，依次输入课程信息和你当前的成绩即可。
#### 代码示例：​​
> **说明**：以下是打开后的代码与说明，也可以直接复制粘贴
```{pyhthon}
print("\n这是深圳大学课程成绩计算器")

# 等级分数范围字典
grade_ranges = {
    'A+': (93, 100),
    'A': (85, 92),
    'B+': (80, 84),
    'B': (75, 79),
    'C+': (70, 74),
    'C': (65, 69),
    'D': (60, 64),
    'F': (0, 59)
}

# 输入课程信息与当前成绩信息
course_name = input("\n请输入课程名称: ")
usual_weight = float(input("请输入平时分占比（如30%输入0.3）: "))
final_weight = float(input("请输入期末考占比（如70%输入0.7）: "))
usual_score = float(input("请输入你目前的平时分成绩: "))

# 显示分数等级对照表
print("\n分数等级对照表:")
for grade, (min_score, max_score) in grade_ranges.items():
    if grade == 'F':
        print(grade,": 60分以下")
    else:
        print(grade,":",max_score-min_score,"分")

# 目标等级选择
target_grade = input("\n请选择并输入目标等级（A+, A, B+, B, C+, C, D, F）: ").upper()

# 计算需要的期末分数
if target_grade in grade_ranges:
    min_target, max_target = grade_ranges[target_grade]
    
    print("\n计算结果（课程: ",course_name,"）:")
    print("平时分:", usual_score ,"分" , "（占比", usual_weight*100 ,"%）")
    print("期末考占比: ",final_weight*100,"%")
    
    # 计算达到目标等级所需的最低和最高期末分数,并保留一位小数
    min_final_needed = min(max(0, (min_target - usual_score * usual_weight) / final_weight),100)
    min_final_needed = round(min_final_needed,1)
    max_final_needed = min(100, (max_target - usual_score * usual_weight) / final_weight)
    max_final_needed = round(max_final_needed,1)
   
    # 输出期末分数
    if min_final_needed  >= 100:
        print("很遗憾，即使期末考满分也无法达到目标等级")
    elif min_final_needed <= 0:
        print("恭喜！你已经达到或超过目标等级")
    else:
        print("\n要达到",target_grade,"等级（",min_target,"-",max_target,"分）:")
        print("期末考需要: ",min_final_needed,"-",max_final_needed,"分")
        print("继续努力，你一定可以的！")
        
else:
    print("输入的目标等级无效，请重新运行程序")

print("\n祝您期末考试顺利！加油！")
```

### 2. 互动猜数字游戏 (题目2.py)
这是一个在命令行中与电脑互动的猜数字小游戏。电脑会随机生成一个数字，您需要开动脑筋猜中它。
#### ​功能特点：​​
- ​随机生成​：每次游戏都会生成一个1到100之间的随机整数。
- ​智能提示​：每次猜测后，程序会告诉您猜大了还是猜小了。
​- 输入验证​：能够处理非法的输入（如输入文字），并提示用户重新输入。
- ​成绩评价​：根据猜中的次数，会给出不同的评价，增加趣味性。
#### ​运行方法：​​
- 下载 *题目2.py* 代码（或复制粘贴代码示例部分代码）。
- 同样需要安装 Python 环境。
- 导航到存放 *题目2.py* 文件的目录。
- 打开程序，游戏开始后，根据提示输入您猜测的数字，享受游戏的乐趣吧！
#### 代码示例：​​
> **说明**：以下是打开后的代码与说明以，也可以直接复制粘贴
```{pyhthon}
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
```
## 学习心得与规划
    我在浏览的时候，发现有人会在GitHub上面记录自己的python学习进度与情况，例如撰写每一次学习后的README.md文件，并上传原代码；有人会分享用Python3编写的各种大小程序，包含从零学Python系列、12306抢票、省市区地址库以及系列网站爬虫等学习源码；有人会推荐好用的代理。这让我觉得，GitHub不仅是代码仓库，更是一个充满活力的学习社区：​持续记录和展示学习过程，本身就是一种高效的学习方法。
    在浏览几个优秀的个人项目后，我发现：优秀的项目不仅仅是代码的堆砌。它们还有清晰的结构、完善的文档、版本管理等。GitHub上 star 数高的项目，（可能别的部分我不完全看得懂，但）无一例外都有一个出色的README.md。它就像是项目的“简历”，解释了项目是做什么的、为什么有用、如何安装、如何使用，因此我也修改并结构化了我的README.md。
    虽然GitHub的访问需要挂梯才能稳定，操作也还在熟悉中，但朋友推荐的CSDN平台让我可以很好的在上面向大家“取经”。未来我计划将继续探索一下这个仓库的其他使用方法，努力将它打造成我的成长型学习日志。我会在上面搜索一些Python、Matlab的有意思的代码并尝试自己编写，有空的话也可以把遇到的问题和解决方案都详细整理在README中。同时，在课程之余，我将利用Github这个平台继续学习Python（例如我发现了有一套175k星的课程：https://github.com/jackfrued/Python-100-Days），或是自学一些其他语言；我也可以跟我的搭子一起在Github这个平台上交流打卡，共同成长。
