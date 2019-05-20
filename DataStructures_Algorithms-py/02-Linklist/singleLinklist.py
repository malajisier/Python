class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    # 创建时默认空链表，head 默认指向头结点
    def __init__(self, node=None):
        self.__head = node

    """判断链表是否为空"""
    def is_empty(self):
        return  self.__head == None

    """链表长度"""
    def length(self):
        # cur游标，用来移动遍历节点
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    """遍历整个链表"""
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    """链表头部添加元素"""
    def add(self, item):

        pass


    """链表尾部添加元素"""
    def append(self, item):
        # 尾部添加新元素 相当于 创建新节点，最后一个节点再指向新节点
        node = Node(item)
        # 链表为空时，指向新节点
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    """指定位置添加元素"""
    def insert(self, pos, item):

        pass



if __name__ == "__main__":
    sll = SingleLinkList()
    print(sll.is_empty())
    print(sll.length())

    sll.append(0)
    sll.append(0)
    sll.append(2)


    print(sll.is_empty())
    print(sll.length())
    print(sll.travel())
