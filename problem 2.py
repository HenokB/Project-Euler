def problem_2():
    a1 = 1
    a2 = 2
    a3 = a1+a2
    sum = a2
    while a3 < 4000000:
        if a3 % 2 == 0: # is it even?
            sum += a3

        a1 = a2
        a2 = a3
        a3 = a1+a2
    print(sum)
    return
problem_2()