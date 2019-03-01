import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#  set up binary tree class


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # print(f'Adding: {value}')
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
        # print(f'Contains: {target}')
        if self.value == target:
            return True
        if self.value > target:
            if self.left and self.left.contains(target):
                return True
            else:
                return False
        elif self.value < target:
            if self.right and self.right.contains(target):
                return True
            else:
                return False


#  initialize tree
tree = BinarySearchTree(names_1[0])

#  add all names from names_1 to tree
for name in names_1:
    tree.insert(name)

#  check if each name in names_2 is already in tree
duplicates = []

for name in names_2:
    if tree.contains(name):
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
