"""
Given a linked list where every node represents a linked list and contains two
pointers of its type:
(i) Pointer to next node in the main list (we call it ‘right’ pointer in below code)
(ii) Pointer to a linked list where this node is head (we call it ‘down’ pointer
in below code).
All linked lists are sorted. See the following example

       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45
Write a function flatten() to flatten the lists into a single linked list. The
flattened linked list should also be sorted. For example, for the above input
list, output list should be 5->7->8->10->19->20->22->28->30->35->40->45->50.
"""

#The idea is to use Merge() process of merge sort for linked lists.
#We use merge() to merge lists one by one. We recursively merge() the
#current list with already flattened list.
#The down pointer is used to link nodes of the flattened list.
def flatten(root):
    if not root or not root.right:
        return root
    return merge(root, flatten(root.right))

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    res = Node()
    if a.val < b.val:
        res = a
        res.down = merge(a.down, b)
    else:
        res = b
        res.down = merge(a, b.down)
    return res
