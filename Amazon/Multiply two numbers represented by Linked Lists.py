"""
Given two numbers represented by linked lists, write a function that returns the
multiplication of these two linked lists.

Examples:

Input : 9->4->6
        8->4
Output : 79464

Input : 3->2->1
        1->2
Output : 3852
"""
# NOTE: This is not a big integer multiplication!
def multiplyTwoLists(first, second):
    num1, num2 = 0, 0
    while first or second:
        if first:
            num1 = num1 * 10 + first.val
            first = first.next
        if second:
            num2 = num2 * 10 + first.val
            second = second.next

    return num1 * num2
