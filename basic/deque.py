class Deque(object):
	def __init__(self):
		self.items = []

	def addRear(self, item):
		self.items.insert(0, item)

	def addFront(self, item):
		self.items.append(item)

	def remRear(self):
		if len(self.items) > 0:
			return self.items.pop(0)
		else :
			print('The Deque is empty. Nothing to remove!')

	def remFront(self):
		if len(self.items) > 0:
			return self.items.pop()
		else :
			print('The Deque is empty. Nothing to remove!')

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []

