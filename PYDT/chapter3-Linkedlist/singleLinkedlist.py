


class Node(object):
    """ 节点 """
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkedlist(object):
    """ 单链表 """
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """ 判断链表是否为空 """
        return self._head == None

    def length(self):
        """ 获取链表长度 """
        # cur游标移动来遍历元素
        cur = self._head
        count = 0

        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """ 遍历链表元素 """
        cur = self._head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        pass

    def append(self, item):
        """ 链表尾部添加元素 """
        # item仅为数据
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node


if __name__ == "__main__":
    sll = SingleLinkedlist()
    print(sll.is_empty())
    print(sll.length())

    sll.append(11)
    print(sll.length())

    sll.append(12)
    sll.append(13)
    sll.append(14)
    sll.append(15)
    sll.travel()

