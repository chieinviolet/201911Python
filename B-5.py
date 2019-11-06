"""
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
"""

nums = [int(e) for e in input("データを入力して下さい>").split(" ")]
# nums = [10, 20, 15]

"""
# sumを使わない合計値
# int はlist を内包することはできない
# split は引数を目印にリストを作る
def goukei():
    goukei_result = 0
    for num in nums:
        goukei_result = goukei_result + num
    print(f'合計値は{goukei_result}です。')
goukei()
"""


# maxを使わない最大値1 numsのindex番号を使って比べる
def original_max():
    max_num = nums[0]
    for i in [0, len(nums) - 2]:
        if nums[i] < nums[i + 1]:
            max_num = nums[i + 1]
        max_num = nums[i]
    print(max_num)


original_max()


# maxを使わない最大値2 numsの中身そのまま比べる
def original_max():
    max_add = 0  # 初期値は0に設定
    for num in nums:
        if num > max_add:
            max_add = num
    print(max_add)

original_max()


# maxを使わない最小値 numsの中身そのまま比べる
def original_min():
    min_add = nums[0]  # 初期値はnums[0]に設定
    for num in nums:
        if num < min_add:
            min_add = num
    print(min_add)
original_min()


# 組み込み関数(mean, len, sum) を使わない 平均値
def original_average():
    total = 0
    total_number = 0
    for num in nums:
        total += num
        total_number += 1
    average_result = total / total_number

    print(average_result)


original_average()
