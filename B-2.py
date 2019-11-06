"""
$ python kuku_2.py
行数を入力してください: 4
列数を入力してください: 6
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24

"""
gyousuu = int(input("行数を入力してください>"))
retsusuu = int(input("列数を入力してください>"))


def kuku_2():
    for a in range(1, gyousuu + 1):
        for b in range(1, retsusuu + 1):
            print(a * b, end=' ')
        print()


kuku_2()
