# coding=utf-8
from time import time

"""
Problem 4
        Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.

解析：
六位数回文数可表示为 xyzzyx
即 pn = 100000x + 10000y + 1000z +100z + 10y + x
      = 100001x + 10010y + 1100z
      = 11( 9091x + 910y +100z )
      = 11ab  （ 即 11ab = 三位数1 * 三位数2 ）
即必然有一个三位数为 11 的倍数
由于乘法互换位置不影响结果, 在此我们认为 第二个三位数为 11 倍数
"""


def if_palindrome(num):
    """
    判断一个数是否为回文数
    :param num: 需要判断的数
    :return: True or False
    """
    num_s = str(num)
    if num_s == ''.join(reversed(num_s)):
        return True
    else:
        return False


if __name__ == '__main__':
    # 初始化最大回文数
    max_n = 0
    # 开始运行时间
    t1 = time()
    # 循环次数
    n = 0
    # 三位数范围为 999-100
    # 因为要求的是最大的回文数，所以逆序进行循环
    for i in range(999, 99, -1):
        # 从 990 开始是因为比 999 小的最大 11 倍数值为 990
        for j in range(990, 99, -11):
            num = i * j
            if if_palindrome(num) and max_n < num:
                max_n = num
            n += 1
    # 结束运行时间
    t2 = time()
    print('最大回文数为： %s\n耗时：%.2fs\n循环次数：%s' % (max_n, t2 - t1, n))
