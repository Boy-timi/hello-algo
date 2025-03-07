'''
File: hashing_search.py
Created Time: 2022-11-26
Author: timi (xisunyy@163.com)
'''

import sys, os.path as osp
sys.path.append(osp.dirname(osp.dirname(osp.abspath(__file__))))
from include import *

""" 哈希查找（数组） """
def hashing_search(map,target):
    # 哈希表的 key: 目标元素，value: 索引
    # 若哈希表中无此 key ，返回 -1
    return map.get(target,-1)

"""  哈希查找（链表） """
def hashing_search1(map,target):
    # 哈希表的 key: 目标元素，value: 节点对象
    # 若哈希表中无此 key ，返回 -1
    return map.get(target,-1)

if __name__=='__main__':
    target=3
    # 哈希查找（数组）
    nums=[1, 5, 3, 2, 4, 7, 5, 9, 10, 8]
    map=dict()                  # 初始化哈希表
    for i in range(len(nums)):
        map[nums[i]]=i          # key: 元素，value: 索引
    index=hashing_search(map,target)
    print("目标元素 3 的索引 = " ,index)

    # 哈希查找（链表）
    head=list_to_linked_list(nums)
    map1=dict()                 # 初始化哈希表
    while head:
        map1[head.val]=head      # key: 结点值，value: 结点
        head=head.next

    node=hashing_search1(map1,target)
    print("目标结点值 3 的对应结点对象为 " , node)
