"""
应用:
1.topK
2.流里面的中值
3.流里面的中位数
优先队列 PriorityBlockingQueue

时间复杂度比较稳定

一个包含 n 个节点的完全二叉树，树的高度不会超过 log2​n

1. 堆排序数据访问的方式没有快速排序友好。(快速排序局部顺序访问，所以对 CPU 缓存友好。)
2. 对于同样的数据，在排序过程中，堆排序算法的数据交换次数要多于快速排序

int 向下取证
round 四舍五入
math.ceil(2.3) 向上取整数
"""

from io import StringIO
import typing
import math


def add_padding(data, pad_length_value):
    data = data.strip()
    return data.center(pad_length_value, ' ')


def swap(data: list, a: int, b: int):
    """
    #swap()函数作用：交换下标为a和b的两个元素
    :param b:
    :param a:
    :param data:
    :return:
    """
    tmp = data[a]
    data[a] = data[b]
    data[b] = tmp


class Heap:
    def __init__(self, capacity: int = 0):
        """
        a: typing.List[int]  # 数组，从下标1开始存储数据
        n: int  # 堆可以存储的最大数据个数
        count: int  # 堆中已经存储的数据个数
        """
        self.a = list(0 for _ in range(capacity + 1))
        self.n = capacity
        self.count = 0

    def insert(self, data: int):
        # O(log n)
        if self.count >= self.n:
            return  # 堆满了

        self.count += 1
        self.a[self.count] = data
        i = self.count

        while int(i / 2) > 0 and self.a[i] > self.a[int(i / 2)]:  # 自下往上堆化
            swap(self.a, i, int(i / 2))  # swap()函数作用：交换下标为i和i/2的两个元素
            i = int(i / 2)

    def remove_max(self):
        if self.count is 0:
            return -1  # 堆中没有数据
        self.a[1] = self.a[self.count]
        self.count -= 1
        self.__heapify(self.a, self.count, 1)

    @staticmethod
    def __heapify(a: typing.List[int],
                  n: int,
                  i: int):
        """
        堆化: 往堆中插入一个元素,调整让其重新满足堆的特性的过程
            自上往下堆化
            堆化的过程是顺着节点所在路径比较交换的，所以堆化的时间复杂度跟树的高度成正比O(log n)
        :param a: 堆数组
        :param n: 堆的长度
        :param i: 从i 开始优化
        :return:
        """
        while True:
            max_pos = i
            if i * 2 <= n and a[i] < a[i * 2]:
                max_pos = i * 2
            if i * 2 + 1 <= n and a[max_pos] < a[i * 2 + 1]:
                max_pos = i * 2 + 1
            if max_pos == i:
                break
            swap(a, i, max_pos)
            i = max_pos

    def build_heap(self,
                   a: typing.List[int],
                   n: int):
        """
        将数组原地建成一个堆
        对下标从 2n​ 开始到 1 的数据进行堆化，下标是 2n​+1 到 n 的节点是叶子节点，不需要堆化。
        实际上，对于完全二叉树来说，下标从 2n​+1 到 n 的节点都是叶子节点。

        O(n)
        :param a:
        :param n:
        :return:
        """
        i = int(n / 2)
        while i >= 1:
            self.__heapify(a, n, i)
            i -= 1

    def sort(self,
             a: typing.List[int],
             n: int):
        """
        堆排序不是稳定的排序算法，因为在排序的过程，
        存在将堆的最后一个节点跟堆顶节点互换的操作，
        所以就有可能改变值相同数据的原始相对顺序。

        O(n log n)
        :param a: 数组a中的数据从下标1到n的位置。
        :param n: n表示数据的个数
        """
        self.build_heap(a, n)
        k = n
        while k > 1:
            swap(a, 1, k)
            k -= 1
            self.__heapify(a, k, 1)

    def show(self):
        output = StringIO()
        pretty_output = StringIO()
        depth = round(math.sqrt(self.count))
        max_row_number = pow(2, depth)
        for index, key in enumerate(self.a):
            if index is 0:
                continue

            if index is not 1 and (index & index - 1) == 0:  # 判断是否是2的n次方
                output.write('\n')
            output.write('%s ' % key if key else 'N ')

            # stage = index // 2 + 1  # 获取当前元素在哪一层
        print('the tree print level by level is :')
        print(output.getvalue())
        print("current tree's depth is %i" % depth)

        output.seek(0)
        pad_length = 3
        keys = []
        spaces = int(math.pow(2, depth))

        while spaces > 1:
            skip_start = spaces * pad_length
            skip_mid = (2 * spaces - 1) * pad_length

            key_start_spacing = ' ' * skip_start
            key_mid_spacing = ' ' * skip_mid

            keys = output.readline().split(' ')  # read one level to parse
            padded_keys = (add_padding(key, pad_length) for key in keys)
            padded_str = key_mid_spacing.join(padded_keys)
            complete_str = ''.join([key_start_spacing, padded_str])

            pretty_output.write(complete_str)

            # add space and slashes to middle layer
            slashes_depth = spaces
            print(f'current slashes depth im_resize: {spaces}')
            print(f"current levle's list is: {keys}")
            spaces = spaces // 2
            if spaces > 1:
                pretty_output.write('\n')  # print '\n' each level

                cnt = 0
                while cnt < slashes_depth:
                    inter_symbol_spacing = ' ' * (pad_length + 2 * cnt)
                    symbol = ''.join(['/', inter_symbol_spacing, '\\'])
                    symbol_start_spacing = ' ' * (skip_start - cnt - 1)
                    symbol_mid_spacing = ' ' * (skip_mid - 2 * (cnt + 1))
                    pretty_output.write(''.join([symbol_start_spacing, symbol]))
                    for _ in keys[1:-1]:
                        pretty_output.write(
                            ''.join([symbol_mid_spacing, symbol]))
                    pretty_output.write('\n')
                    cnt = cnt + 1

        print(pretty_output.getvalue())
