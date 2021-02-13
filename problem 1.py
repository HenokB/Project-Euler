def Problem1():
    start_sum = 0
    for i in range(1000):
        if i%3==0 or i%5==0:
            start_sum += i
    return start_sum
Problem1()