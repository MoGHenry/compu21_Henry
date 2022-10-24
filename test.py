class ListNode:
    def __init__(self, x: 0):
        self.val = x
        self.next = None

    @staticmethod
    def creat_list(lists):
        head = cur = ListNode(0)
        for i in lists:
            next_node = ListNode(i)
            cur.next = next_node
            cur = cur.next
        return head.next


a = ListNode(0)
c = [1, 2, 3, 4]
d = [3, 4]
a = a.creat_list(c)
b = ListNode(0)
b = b.creat_list(d)

dict = {1: b}
if b in dict.values():
    print("true")
if a in dict.values():
    print("false")

# while a:
#     print(a.val)
#     if a.next:
#         print(a.next.val)
#     print("-----------")
#     a = a.next
