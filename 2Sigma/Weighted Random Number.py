"""
可以存 key ( string ) 和其对应的 weight (int)
2. 可以call randomPick() API，按照每个 key 的 weight 在 total weight 里面的占比，
来返回一个 random key.

e.g.
a -> 10.
b -> 20 .
Prob(return a) -> 1/3
prob(return b) -> 2/3

算法题:
给一个object with weights, 然后设计两个函数 put(object, weight), get().
其中get要返回对应object, 而且是要按照weights等概率的返回.

解法:
Brute force: 开一个数组, 然后weight是几就重复存几个数字, 然后rand() % size返回即可
空间优化: 数组存元素及对应的weights, 这样求出rand number数个数找到对应object 返回
时间优化: Augmented BST: 每个BST多加一个data member: size 来track 其subtree的weights总和.
"""
from random import uniform, randint

class WeightedRandomNumber(object):

    def __init__(self):
        self.total = 0
        self.weights = {}

    def set(self, key, weight):
        if key in self.weights:
            self.total -= self.map[key]
        self.total += weight
        self.weights[key] = weight

    def get(self):
        cur = uniform(0, self.total)
        sum = 0
        for key in sorted(self.weights.keys()):
            sum += self.weights[key]
            if sum >= cur:
                return key

w = WeightedRandomNumber()
w.set('A', 10)
w.set('B', 10)
w.set('C', 20)
w.set('D', 60)

w.set('A', 1.01)
w.set('B', 1.01)
w.set('C', 2.01)
w.set('D', 6.01)

from collections import Counter
m = Counter()
for i in range(1000):
    m[w.get()] += 1
print m



# def myRand(keys, weights, n):
#     # is weights always int? is keys and weights already sorted?
#     keys = sorted(keys)
#     weights = sorted(weights)
#     total = sum(weights)
#     target = uniform(0, total)
#     cur = 0
#     for i in range(len(keys)):
#         cur += weights[i]
#         if cur >= target:
#             return keys[i]
#
# # Optimize 1: make for loop binary serch O(log N)
# def find(target, keys, weights):
#     i = 0
#     j = len(keys) - 1
#     while i + 1 < j:
#         m = (i+j) / 2
#         if weights[m] < target:
#             i = m
#         else:
#             j = m
#     return keys[j]
#
# # Optimize 2:  keeping an array M where M[i] stores the element corresponding
# # to point i. This allows us to return the area immediately from the array O(1)
#
# keys = ['A', 'B', 'C']
