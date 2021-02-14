import fractions
from math import gcd


def problem5():
    solution = 1
    for i in range(1, 21):
        solution *= i // fractions.gcd(i, solution)
    return str(solution)

print(problem5())


# using the worst case possible and doing it in the worst way. I challenge you to write a worse one.
def pr(x):
    a = []
    for i in range(1,x):
        if (i % 2 ==0 and i % 3==0 and i % 4==0 and i % 5 ==0 and i % 6==0 and i % 7==0 and i % 8 ==0 and i % 9==0 and i % 10==0 and i % 11 ==0 and i % 12 ==0 and i % 13==0 and i % 14==0 and i % 15 ==0 and i % 16==0 and i % 17==0 and i % 18 ==0 and i % 19==0 and i % 20==0):
            a+=[i]
    return min(a)