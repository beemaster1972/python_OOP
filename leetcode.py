class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        graph = collections.defaultdict(list)          # build graph
        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)
        d = dict()                                     # {index: min_index_of_connected_indicess}
        @lru_cache(None)                               # dfs on connected indices
        def dfs(i):
            nonlocal c, d, min_i
            for nei in graph[i]:
                if nei not in d:
                    c[source[nei]] += 1                # counting available values & their freqencies
                    d[nei] = min_i                     # index: min_index_of_connected_indices
                    dfs(nei)
        for i, num in enumerate(source):               # for each value in source O(N)
            if i not in d:                             # if not visited yet
                min_i = d[i] = i                       # set min_i: min_index_of_connected_indices
                c = collections.defaultdict(int)       # initialize counter (Counter() is also ok)
                c[num] = 1
                dfs(i)                                 # dfs on all neighboors (nei)
                d[i] = c                               # d[min_index_of_connected_indices] is a dictionary,
                                                       # but all its neighboors will have
                                                       # d[nei] = min_index_of_connected_indices (an integer)
        ans = 0
        for i, tar in enumerate(target):               # calculate hamming distance in a greedy way
            if isinstance(d[i], int):                  # if d[i] is an integer, we need to find its `min_index_of_connected_indices`
                                                       # d[d[i]] is the dict counting connect values & frequencies
                if d[d[i]][tar] > 0: d[d[i]][tar] -= 1 # if available, frequency minus 1
                else: ans += 1                         # if not available, ans += 1
            else:                                      # if d[i] is a defaultdict, then `i` itself is `min_index_of_connected_indices`
                if d[i][tar] > 0: d[i][tar] -= 1       # if available, frequency minus 1
                else: ans += 1                         # if not available, ans += 1
        return ans

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