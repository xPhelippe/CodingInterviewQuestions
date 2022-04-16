class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self,data = None):
    self.head = Node(data)

  def add(self,data=None):
    if data is None:
      return

    cur = self.head

    while cur.next is not None:
      cur = cur.next

    cur.next = Node(data)

  def print(self):
    cur = self.head
    while cur is not None:
      print(cur.data,end=" ")
      cur = cur.next
    print()

  def getHead(self):
    return self.head

ll = LinkedList(3)
ll.add(5)
ll.add(8)
ll.add(5)
ll.add(10)
ll.add(2)
ll.add(1)

ll.print()

def partition(head,part):

  if head is None:
    return 
  
  lowhead = Node()
  low = lowhead

  highhead = Node()
  high = highhead

  while head is not None:
    if head.data < part:
      low.next = Node(head.data)
      low = low.next  
    else:
      high.next = Node(head.data)
      high = high.next

    head = head.next

  low.next = highhead.next
  return lowhead.next

end = partition(ll.getHead(),5)

while end is not None:
  print(end.data,end=" ")
  end = end.next
  

  