# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 10:54:12 2025

@author: binia
"""
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