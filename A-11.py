"""
# 例
$ python bmi.py
Height(m)? > 170
Weight(kg)? > 60
Your BMI is 20.76
"""
height = float(input("Height(M)?>"))
weight = int(input("weight(Kg)?>"))


def BMI_value(height, weight):
    return round(weight / (height ** 2), 2)


print(f'Your BMI is {BMI_value(height, weight)}')

# Height(m)? > 170
# Weight(kg)? > 60
# Your BMI is 20.76
