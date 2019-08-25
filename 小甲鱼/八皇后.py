def conflict(nextX, state):
    nextY = len(state)
    for i in range(len(state)):
        if abs(nextX - state[i]) in (0, nextY - i):
            return False
    return True


def my_queen(num, state=()):
    """
    # 八皇后的递归和yield理解之我见
    # 首先是为什么要使用yield，我们选择的是函数，如果用 return 函数一到这里就结束了，所以一般递归的函数除非return自己，yongyield使得函数挂起更好
    # 关于递归的解释，我是这样想的：
    # 八皇后有八个层级的迭代，相当于八个老板
    # 首先大老板一拍脑袋，说第一个是0到7中间任何一个，找来二老板，叫他帮忙找后面的七个数，二老板完成的结果就是my_queen(num, (pos,)),给到大老板，大老板把自己
    # 一拍脑袋的数加到前面，就是最终的结果，这就是为什么pos在result前面
    # 二老板拿到大老板的指令后，立马找能接在后面的几个数，然后告诉三老板，前两个是（0，1），你给我找出后面的几个
    # 三老板拿到二老板给的条件，自己再做一遍筛选，找出前三个元素，例如前三个是（0，2，5），叫四老板帮他找后面的
    # 。。。。
    # 七老板终于找到前面七个了，这就好办了，最后一个人找到跟前面七个满足条件的数，大功告成
    # #######################################################################################################
    # 注意到当棋盘是2或者3时，是没有解的，这说明：
    # 有一个问题，当棋盘是两个的时候，大老板找到0，1交给二老板，二老板找不到，所以没办法yield，这时候就是空结果
    # 特别当棋盘大小为2，3的时候，函数生成的结果是空，这就说明yield语句没有被执行。
    :param num:
    :param state:
    :return:
    """
    for pos in range(num):
        if conflict(pos, state):  # 只剩最后一个，直接加到末尾
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in my_queen(num, state + (pos,)):  # 当八皇后的顺序没有到最后一个时，需要将刚刚不冲突的作为state参数传进去
                    yield (pos, ) + result



def pretty_print(state):
    num = len(state)
    for pos in state:
        print('-' * pos + '#' + '-' * (num - pos - 1))


if __name__ == '__main__':
    for i in my_queen(8,(0,)):
        print(i)
