# coding=utf-8
'''
Problem 3
        Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
from math import sqrt


def isPrime(n):
    '''
    判断一个数是否为质数
    :param n: 需要判断的整数
    :return: 质数返回 True , 非质数返回 False
    '''
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


num = 600851475143
# 初始答案值
result = 0
# 初始因子
factor = 2
while factor <= num:
    if all([isPrime(factor), num % factor == 0]):
        result = factor
        num /= factor
        # print(num)
    factor += 1
# 不能用 for , for 之后循环次数已固定
# 之后更改 num 值无效
# for i in range(2, num + 1):
#     if all([isPrime(i), num % i == 0]):
#         num /= i
#         print(num)
#         result = i

# 答案
print(result)
