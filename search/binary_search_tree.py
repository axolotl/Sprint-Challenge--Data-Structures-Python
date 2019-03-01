from queue import *


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        #  initialize stack to store nodes
        stack = []
        #  start with root node
        stack.append(self)
        #  loop while stack is not empty
        while len(stack):
            #  pop from stack, adding right and left children
            current = stack.pop()
            #  call our callback
            cb(current.value)
            #  add right, then add to stack
            if current.right:
                stack.append(current.right)
            #  if left, add to stack
            if current.left:
                stack.append(current.left)

    def breadth_first_for_each(self, cb):
        #  inialize a queue to store nodes
        queue = Queue()
        #  start with root node
        queue.put(self)
        #  loop while stack is not empty
        while not queue.empty():
            #  dequeue next item
            current = queue.get()
            #  run callback
            cb(current.value)
            #  add left and right children
            if current.left:
                queue.put(current.left)
            if current.right:
                queue.put(current.right)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
