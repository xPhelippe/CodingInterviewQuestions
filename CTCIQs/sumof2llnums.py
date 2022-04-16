class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = Node()

  def add(self,data=None):
    if data is None:
      return

    cur = self.head
    while cur.next is not None:
      cur = cur.next
    cur.next = Node(data)

  def print(self):
    cur = self.head.next

    while cur is not None:
      print(cur.data,end=" ")
      cur = cur.next

    print("")

  def getHead(self):
    return self.head.next

l1 = LinkedList()
l1.add(1)

l2 = LinkedList()
l2.add(9)
l2.add(9)
l2.add(9)

l1.print()
l2.print()

def sumLL(l1, l2):

  carry = 0

  end = Node()
  cur = end
  
  while True:
    if l1 is None and l2 is None:
      break
    
    if l1 is None:
      v1 = 0
    else:
      v1 = l1.data

    if l2 is None:
      v2 = 0
    else:
      v2 = l2.data

    sum = carry + v1 + v2

    carry = int(sum / 10)
    sum = sum % 10

    cur.next = Node(sum)
    cur = cur.next

    if l1 is not None:
      l1 = l1.next

    if l2 is not None:
      l2 = l2.next

  if carry > 0:
    cur.next = Node(1)

  return end.next

res = sumLL(l1.getHead(),l2.getHead())

while res is not None:
  print(res.data,end=" ")
  res = res.next

print("")
