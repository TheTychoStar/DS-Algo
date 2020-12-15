# Python Basics

> This project is to demonstrate how to implement the local Python programs in *Shell*, as well as practice the basic Git operations learned from the Data Science Bootcamp - Algorithmic Trading Class.

## python_store.py

In this file, several storing method in Python have been introduced with the related syntax.

Please check the detail content in the following:

## Python Important Data Structure

- **list**
used to store multiple items in a single variable.

  > one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary,

- **deque**
is implemented using the module “collections“.

  > Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.

- **dictionary**
used to store data values in key:value pairs.

  > A dictionary is a collection which is unordered, changeable and does not allow duplicates.

- **tree**
represents the nodes connected by edges. It is a non-linear data structure.
  
    1. One node is marked as Root node.
    2. Every node other than the root is associated with one parent node.
  3. Each node can have an arbitrary number of child node.
  
    For more information, please check this video: [heapsort](https://www.bilibili.com/video/av47196993/)

## Quick view

|                | list             | deque                   | dictionary  | tree                     |
| :------------: | ---------------- | ----------------------- | ----------- | ------------------------ |
| require module | default          | collections             | default     | binarytree               |
|     define     | [value1, value2] | deque([value1, value2]) | {key:value} | Node(value, left, right) |

