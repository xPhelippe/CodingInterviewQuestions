class StackQueue:
  def __init__(self):
    self.mains = []
    self.sides = []

  def add(self, el=None):
    if el is None:
      return

    if len(self.mains) == 0:
      self.mains.append(el)
      return
    else:

      # move elements to side stack
      while len(self.mains) > 0:
        self.sides.append(self.mains.pop())

      self.mains.append(el)

      # move elements back to main stack
      while len(self.sides) > 0:
        self.mains.append(self.sides.pop())


  def remove(self):
    if len(self.mains) > 0:
      el = self.mains.pop()
      return el
    
  def peek(self):
    if len(self.mains) > 0:
      el = self.mains.pop()
      self.mains.append(el)
      return el

  def print(self):
    while len(self.mains) > 0:
      self.sides.append(self.mains.pop())

    while len(self.sides) > 0:
      el = self.sides.pop()
      print(el,end=" ")
      self.mains.append(el)
    print("")

sq = StackQueue()

sq.add(1)
sq.add(2)
sq.add(3)
sq.add(4)

sq.print()

print(sq.peek())

sq.remove()

# sq.print()

sq.add(8)
sq.add(9)

sq.print()

sq.remove()
sq.print()

