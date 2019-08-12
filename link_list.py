"""
    单链表学习程序
    重点程序
"""
#改改改第而种方法
# 哈哈哈哈
# 创建结点类
class Node(object):
    def __init__(self, value, next=None):
        self.value = value  # 有用数据
        self.next = next


# 链表的操作:
class Linklist(object):
    def __init__(self):
        # self.head = None
        self.head = Node(None)

    def init_list(self, list):
        # self.head = Node(None) #链表的开头
        p = self.head  # 可移动变量
        for i in list:
            p.next = Node(i)
            p = p.next

    def show(self):
        p = self.head.next
        while p:
            print(p.value, end=' ')
            p = p.next
        print()

    def my_add(self, value):
        p = self.head.next
        while p:
            if p.next == None:
                break
            p = p.next
        p.next = Node(value)

    def my_ad(self, list, value):
        p = self.head
        for i in list:
            p.next = Node(i)
            if p.next == None:
                break
            p = p.next
        p.next = Node(value)

    # 尾部插入新的结点
    def append(self, item):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(item)

    # 获取链表长度
    def get_length(self):
        count = 0
        p = self.head
        while p.next is not None:
            count += 1
            p = p.next
        return count

    # 判断链表是否为空
    def is_empty(self):
        if self.get_length() == 0:
            return True
        else:
            return False

    def is_e(self):
        p = self.head
        if p.next == None:
            return True
        return False

    # 清空列表
    def clear(self):
        self.head.next = None

    def get_item(self, index):
        count = 0
        p = self.head.next
        if index >= self.get_length():
            raise IndexError("list index out of range")
        while p is not None:
            count += 1
            p = p.next
            if count == index:
                return p.value

    # 获取链表索引值
    def get_msg(self,index):
        count = 0
        p = self.head.next
        while count < index and p is not None:
            count += 1
            p = p.next
        if p is None:
            raise IndexError("list index out of range")
        else:
            return p.value

    # def fun01(self,index):
    #     count = 0
    #     p = self.head
    #     while count < index and p is not None:
    #         count += 1
    #         p = p.next
    #         if p is None:
    #             raise IndexError("list index out of range")
    #         else:
    #             return p
    # def insert(self,index,item):
    #     p = self.head
    #     self.fun01(index)
    #     Node(item).next = p.next
    #     p.next = Node(item)

    #插入
    def t(self,index,item):
        if index < 0 or index > self.get_length():
            raise IndexError("list index out of range")
        p = self.head
        i = 0
        while i < index:
            p = p.next
            i += 1
        Node(item).next = p.next
        p.next = Node(item)

    #删除
    def delete(self,item):
        p = self.head
        while p.next is not None:
            if p.next.value == item:
                p.next = p.next.next
                break
            p = p.next






    # def my(self,value):
    #     a = Node(value)
    #     p = self.head
    #     while True:
    #         if p.next == None:
    #             break
    #         p = p.next
    #     p.next = a


if __name__ == "__main__":
    # 创建列表对象
    link01 = Linklist()
    # 创建数据
    list01 = [1, 2, 3, 4, 5, 6]
    # link01.init_list(list01)  # 将初始数据插入列表
    link01.my_ad(list01, 8)
    link01.show()
    print(link01.get_length())
    # print(link01.is_empty())
    print(link01.is_e())
    # link01.clear()
    # print(link01.is_empty())
    print(link01.is_e())
    # print(link01.get_item(2))
    # print(link01.insert(2,10))
    # link01.t(2, 10)
