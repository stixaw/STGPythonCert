import os
import sys
import numtostring
import fibonacci


def fib_looper(n):
    # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
    if n <= 1:
        result = n
        print(n)

    else:
        fib_list = [0, 1]
        i = 2
        while i < n + 1:
            fib_list.append(fib_list[i - 2] + fib_list[i - 1])
            i += 1
        for num in fib_list:
            num_word = numtostring.get_num(num)
            print("{} ... {}".format(num, num_word), end=' ')


if __name__ == '__main__':
    fib_looper(8)
