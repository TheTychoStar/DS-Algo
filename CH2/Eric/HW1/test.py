import collections
d = collections.deque([1,2,3])
print(f'd={d}')
d.appendleft(0)
print(f'append 0 to the left: d={d} ')
d.extendleft([-1,-2])
print(f'extend [-1,-2] to the left: d={d} ')
d.rotate(1)
print(f'rotate 1: d={d} ')
d.rotate(-1)
print(f'rotate -1: d={d} ')
d.rotate(10)
print(f'rotate 10: d={d} ')

