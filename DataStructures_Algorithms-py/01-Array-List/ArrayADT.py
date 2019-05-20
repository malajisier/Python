from array import array

# 实现定长的Array ADT
class Array(object):
    def __init__(self, size=32):
        self.size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items(index)

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def __clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter(self):
        for item in self._items:
            yield item

arr = array('u', 'asdf')
print(arr[0], arr[1], arr[2], arr[3])

def test_array():

    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1
    assert len(a) == 10
