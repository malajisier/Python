import math

radius = float(input('请输入半径： '))
length = 2 * math.pi * radius
area = math.pi * (radius ** 2)
print('length: %.2f, area: %.2f' % (length, area))