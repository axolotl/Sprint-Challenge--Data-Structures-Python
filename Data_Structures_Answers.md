Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

The complexity is O(n) where n in the number of nodes.

2. What is the space complexity of your `depth_first_for_each` function?

At any given time, the most nodes we'll have on the stack will equal the right right and left branches for a given path all the way to our leaf nodes. In a perfectly balanced tree, the number of layers will increment once per each doubling of the number of nodes. Thus, our space requirement is log(n) where n is the number of nodes. In the worst case unbalanced tree our space complexity may be up to n.

3. What is the runtime complexity of your `breadth_first_for_each` method?

The complexity is O(n) where n in the number of nodes.

4. What is the space complexity of your `breadth_first_for_each` method?

In a breadth first search, the most nodes we'll ever have in memory will be all of the nodes at a given depth layer. Given the binary nature of our tree, the number of nodes at the deepest layer will contain at most 2 to the power of the height of our tree.

5. What is the runtime complexity of the provided code in `names.py`?

The complexity is O(n \* m) where n is the length of names_1 and m is the length of names_2. This is because each name must be compared with each other name.

6. What is the space complexity of the provided code in `names.py`?

The space complexity is is O(n + m) where n is the length of names_1 and m is the length of names_2. We don't need any additional memory.

7. What is the runtime complexity of your optimized code in `names.py`?

The runtime complexity is n log n for the creation of the tree and log n for each duplicate.

8. What is the space complexity of your optimized code in `names.py`?

Because we create another data structure with one node per item in array_1, our complexity is O(2n + m). Dropping constants it's O(n + m).
