from time import time
import random

def summation(n):
    result = 0
    for i in range(1, n+1):
        result += i
    print(result)
    return result

def summation2(n):
    print((n/2*(n+1)))
    return (n/2*(n+1))

def analyze_algo(n=1):
    stime = time()
    summation(n)
    etime = time()
    elapsed = etime-stime
    print("execution time: ", elapsed)

def analyze_algo2(n=1):
    stime = time()
    summation2(n)
    etime = time()
    elapsed = etime-stime
    print("execution time2: ", elapsed)

#7.2
def randomList(n):
    return list(random.sample(range(100000), n))

def isIntersect(a, b, c):
    all_list = a+b+c
    for i in all_list:
        result = all_list.count(i)
    if result == 3:
        return True
    else:
        return False

def isIntersect2(a, b, c):
    for i in a:
        for j in b:
            for k in c:
                if i == j and i == k:
                    return True
    else:
        return False

def analyze_algo3(n=1):
    lsta = randomList(n)
    lstb = randomList(n)
    lstc = randomList(n)

    stime = time()
    print(isIntersect(lsta, lstb, lstc))
    etime = time()
    elapsed = etime-stime
    print("execution time1: ", elapsed)

    stime = time()
    print(isIntersect2(lsta, lstb, lstc))
    etime = time()
    elapsed = etime-stime
    print("execution time2: ", elapsed)


def main():
    # analyze_algo(1000000000)
    # analyze_algo2(1000000000)
    analyze_algo3(10000)

main()