# Project-Euler
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
#Some Project Euler problems
#You can find all the problems here: https://projecteuler.net/about

![Happy Christmas](web.png)

# Project Euler problem and solutions




### [1. Problem 1](./problem 1.py)

-If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

```py
def Problem_1():
    start_sum = 0
    for i in range(1000):
        if i%3==0 or i%5==0:
            start_sum += i
    return start_sum
Problem_1()
```
