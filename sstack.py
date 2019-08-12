"""
栈的顺序存储结构
重点代码
"""

# 自定义栈异常
class StackError(Exception):
    pass
#基于列表实现顺序栈
class SStack:
    def __init__(self):
        #约定列表的最后一个元素为栈顶元素
        self._elms = []

    def top(self):
        if not self._elms:
            raise StackError("stack is empty")
        return self._elms[-1]

    #判断栈是否为空
    def is_empty(self):
        return self._elms == []

    #入栈操作
    def push(self,elem):
        self._elms.append(elem)

    #出栈操作
    def pop(self):
        if not self._elms:
            raise StackError("stack is empty")
        return self._elms.pop()



if __name__ == "__main__":
    st =SStack() #初始化栈
    # print(st.top())



