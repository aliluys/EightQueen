
count = 0


def hanoi(number, x, y, z):
    global count
    if number == 1:
        # print('step %d' % count, x, '======>', z)
        count += 1
        return
    #  把前n-1个移动到中间，再把最后一个移到中间
    hanoi(number - 1, x, z, y)
    # print('step %d'%count, x, '======>', z)
    count += 1
    hanoi(number - 1, y, x, z)


if __name__ == '__main__':
    number = int(input('输入一个正整数：'))
    res = hanoi(number, 'A', 'B', 'C')
    print(count)