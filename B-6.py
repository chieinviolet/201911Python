"""
N面サイコロをM回振ったときの結果を表示してください
N, M は正の整数とします
N, M はユーザーからの入力を利用すること
"""
import random

N = int(input('何面のサイコロを振りますか？>'))
M = int(input('サイコロは何回振りますか？>'))


# N = 3
def dice_number():
    print(f'サイコロの目は{random.choices(range(1, N + 1), k=M)}')


dice_number()
