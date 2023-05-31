def min_ham_dist(source, target, allowedSwaps):



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    __tail = None
    __length = 0

    def __get_list_length(self, head):
        cur_node = head
        i = 0
        while cur_node:
            i += 1
            cur_node = cur_node.next
        return i

    def __get_node(self, head, indx):
        cur_node = head
        i = 1
        indx = indx if indx > 0 else self.__length + indx + 1
        while cur_node:
            if i == indx:
                return cur_node
            i += 1
            cur_node = cur_node.next

    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        self.__length = self.__get_list_length(head)
        swap_node_1 = self.__get_node(head, k)
        swap_node_2 = self.__get_node(head, -k)
        swap_node_1.val, swap_node_2.val = swap_node_2.val, swap_node_1.val
        return head