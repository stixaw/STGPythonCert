import fibonacci
import numtostring
import inflect

p = inflect.engine()


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
            num_word = p.number_to_words(num)
            print("{} ... {}".format(num, num_word))


def fib_looper2(n):
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
            num_word = numtostring.is_number_positive(num)
            print("{} ... {}".format(num, num_word))


# , end=' '

if __name__ == '__main__':
    fib_looper(30)
    fib_looper2(5)
