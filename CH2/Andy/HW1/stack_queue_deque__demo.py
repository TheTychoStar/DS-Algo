# demo of stack v.s queue v.s deque

# i. Stack behavior (LIFO)
stack = ['x' + str(i) for i in range(5)]
'''>>> [x0, x1, x2, x3, x4]'''

stack.pop()  # remove x4
stack
'''>>> [x0, x1, x2, x3]'''

# ii. Queue behavior (FIFO)
queue = ['x' + str(i) for i in range(5)]
'''>>> [x0, x1, x2, x3, x4]'''

queue.pop(0)  # remove x0
queue
'''>>> [x1, x2, x3, x4] '''

# iii. Deque (i.e. Double Ended Queue)
deq = ['x' + str(i) for i in range(5)]
'''>>> [x0, x1, x2, x3, x4]'''

from collections import deque
deq = deque(deq)
'''>>> deque(['x0', 'x1', 'x2', 'x3', 'x4'])'''

deq.pop()  # remove x4
deq
'''>>> deque(['x0', 'x1', 'x2', 'x3'])'''

deq.popleft()  # remove x0; list cannot do this
'''>>> deque(['x1', 'x2', 'x3'])'''

deq.append('x4')  # append x4 to the rightmost end
'''>>> deque(['x1', 'x2', 'x3', 'x4])'''

deq.appendleft('x0')  # append x0 to the leftmost end; list cannot do this
'''>>> deque(['x0', 'x1', 'x2', 'x3', 'x4])'''

deq.extend(['x5', 'x6'])  # concat ['x5', 'x6'] to the right; list can do this
'''>>> deque(['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'])'''

deq.extendleft(['x-1', 'x-2'])
# concatenate ['x-2', 'x-1'] to the left; note the order
'''>>> deque(['x-2', 'x-1', 'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'])'''

deq.extend('abc')  # concat ['a','b','c'] to the right; list raise error
'''>>> deque(['x-2', 'x-1', 'x0','x1','x2','x3','x4','x5','x6','a','b','c'])'''

deq.extendleft('de')  # concat ['d','b','c'] to the right; list raise error
'''>>> deque(['e','d','x-2','x-1','x0','x1','x2','x3','x4','x5','x6','a','b','c'])'''
