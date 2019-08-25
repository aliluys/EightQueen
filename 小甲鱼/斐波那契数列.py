def fibonacci(n):
    n1 = 1
    n2 = 1
    n3 = 1

    while n>2:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1
    return n3


def fibonacci2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)


def timer(func):
    import time

    def wrapper(*args, **kwargs):
        s = time.time()
        res = func(*args, **kwargs)
        e = time.time()
        print('程序耗时%.20f秒' % (e-s))
        return res
    return wrapper


if __name__ == '__main__':
    fibonacci = timer(fibonacci)
    # fibonacci2 = timer(fibonacci2)

    res = fibonacci(10000)
    print(res)
    # fibonacci2(100)


