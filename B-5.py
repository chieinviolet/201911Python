"""
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
"""
nums = [int(e) for e in input("データを入力して下さい>").split(" ")]


# sumを使わない合計値
# int はlist を内包することはできない
# split は引数を目印にリストを作る
def goukei():
    goukei_result = 0
    for num in nums:
        goukei_result = goukei_result + num
    print(f'合計値は{goukei_result}です。')
goukei()
