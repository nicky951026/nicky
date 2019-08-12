"""
链式队列
重点代码
"""

# 创建结点类
class Node(object):
    def __init__(self, value, next=None):
        self.value = value  # 有用数据
        self.next = next

# 队列异常
class QueueError(Exception):
    pass

#队列结点类
class LQueue:
    def __init__(self):
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front is self.rear

    def enqueue(self,elem):
        self.rear.next = Node(elem)
        self.rear = self.rear.next

    def clear(self):
         self.rear = self.front

    def denqueue(self):
        if self.front is self.rear:
            raise QueueError("Queue is empty")
        self.front = self.front.next
        return self.front.value

if __name__ == "__main__":
    lq = LQueue()
    print(lq.is_empty())
    lq.enqueue(10)
    lq.enqueue(90)
    while lq.rear is not lq.front:
       print(lq.denqueue())

