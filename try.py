class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

c = ListNode(3,None)
b = ListNode(2,c)
a = ListNode(1,b)

t1 = a
t2 = b
for i in range(2):   #兩個兩個互換作業
    tn = t1
    tnn = t2.next
    t1 = t2
    t2.next = tn
    t2 = tnn
    #t1,t2,t2.next = t2,t2.next,t1

print(b.next.val,c.next.val)
