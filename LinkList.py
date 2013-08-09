#!/usr/bin/python

class LLNode:
	def __init__(self, key, payload, next = None):
		self.key     = key
		self.payload = payload
		self.next    = next

class LinkList(LLNode):
	def __init__(self):
		self.next    = None
		self.key     = None
		self.payload = None

	
	def locateNode(self, key, previous = False):
		if key is None:
			return None
		
		node = self

		while True:
			if node.next is None:
				return node

			if node.next.key > key:
				return node
			
			if node.next.key == key:
				if previous:
					return node
				else:
					return node.next
			
			node = node.next


	def __contains__(self, key):
		node = self.locateNode(key)

		if node:
			return node.key == key

		return None
		
		
	def __getitem__(self, key):
		node = self.locateNode(key)
		
		if node.key == key:
			return node.payload

		return None


	def remove(self, key):
		node = self.locateNode(key, True)
		
		if node is None:
			# Not found, but still OK.
			return True
		
		if node.next :
			if node.next.key == key:
				# Here is it
				n = node.next.next
				# not really need because of GC, but anyway
				del node.next
				
				node.next = n
		

	def __delitem__(self, key):
		return self.remove(key)
	

	def add(self, key, payload):
		node = self.locateNode(key)
		
		if node is None:
			return False
		
		if node.key == key:
			# Already in the list, replace the payload
			# not really need because of GC, but anyway
			del node.payload
			node.payload = payload
			return True

		n = node.next
		node.next = LLNode(key, payload, n)

		return True


	def __setitem__(self, key, payload):
		return self.add(key, payload)


	def dump(self):
		node = self
		
		i = 0

		while True:
			if node.next is None:
				return

			print "%10d %-30s %s" % (i, node.next.key, node.next.payload)
			
			i += 1
			
			node = node.next


if __name__ == "__main__" :
	ll = LinkList()
	ll["Niki"]	= "Sofia"
	ll["Alex"]	= "Bourgas"
	ll["Boris"]	= "USSR"
	ll["Zoro"]	= "Mexico"

	print "Niki" in ll
	
	print ll["Niki"]

	del ll["Niki"]
	
	print "Niki" in ll
	
	print ll["Niki"]	

	ll.dump()


