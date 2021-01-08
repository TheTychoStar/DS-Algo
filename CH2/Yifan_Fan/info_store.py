# encoding: utf-8
'''
 This program is to demonstrate the basics operations of the main information
 storing process in Python.

 Author: Yifan Fan
 Email: yfan9981@gmail.com
 Date: Dec.15 2020
 Created for the practice of DS Algo Class
'''

from collections import deque


def list_demo():
    # List Demonstration

    # Create:
    my_list = ['apple', 'banana', 'cherry']
    print('Firstly, using [] to build a list:{}'.format(my_list))
    print('Here is the length:{}'.format(
        len(my_list)
    ))
    mix_list = [123, 'apple', True, 12.5]
    print('A list can also contain different data types:{}'.format(mix_list))
    print('Nested list is also allowed:{}'.format(
        [my_list, mix_list]
    ))

    # Slicing:
    print('Slicing lists by using [start:end:step]')
    seq_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(seq_list[8:2:-1])

    print('List is mutable.')
    seq_list[0] = 0
    print(seq_list)

    print('It is also iterable.')
    seq_list = [x for x in range(1, 11)]
    for x in seq_list:
        print(x)

    # Sorting:
    print('Use sort() method to sort a list:')
    seq_list.sort(reverse=True)
    print(seq_list)

    # Copying:
    print('A list can not be simply copied by using list_2 = list_2,\n'
          'Since list_2 will only be a reference to list_1.\n'
          'Use the copy() method.')

    # Adding:
    print('Join two or more lists by using the + operator:')
    add_list = my_list + mix_list
    print(add_list)
    print('Obviously it also support the duplicated items.')
    print('use append() to add an element at the end.')
    seq_list.append(11)
    print(seq_list)
    print('and use pop() to remove it.')
    seq_list.pop()
    print(seq_list)

    # ask to leave the program:
    input('Press any key to leave.')


if __name__ == '__main__':
    list_demo()
