#!/usr/bin/python


from random import random


class LLNode:
	def __init__(self, key, payload):
		self.key     = key
		self.payload = payload
		
		self.x_next  = None

	def chk_next(self, rail = 0):
		if self.x_next is None:
			self.x_next = []
		
		while len(self.x_next) <= rail:
			self.x_next.append(None)
	
	def next(self, rail = 0):
		self.chk_next(rail)
		
		return self.x_next[rail]

	def set_next(self, node, rail = 0):
		self.chk_next(rail)
		
		self.x_next[rail] = node


class LinkList(LLNode):
	def __init__(self, max_rail):
		LLNode.__init__(self, None, None)
		
		self.max_rail = max_rail
	
	
	def locateNode(self, key, stop_rail = 0, previous = False):
		if key is None:
			return None
		
		self.log( "Find %s" % key )
		
		node = self
		rail = self.max_rail
		
		while rail > stop_rail:
			rail -= 1
			
			self.log( "\tRail %d" % rail )
			
			while True:
				if node != self:
					self.log(  "\t\tTry %s" % node.key )

				if node.next(rail) is None:
					break

				if node.next(rail).key > key:
					break
				
				if node.next(rail).key == key:
					self.log(  "\t\tFound !!!" )
					if previous:
						return node
					else:
						return node.next(rail)
				
				node = node.next(rail)

		return node


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


	def remove(self, key, rail = 0):
		node = self.locateNode(key, previous = True)
		
		if node is None:
			# Not found, but still OK.
			return True
		
		if node.next(rail) :
			if node.next(rail).key == key:
				# Here is it
				n = node.next(rail).next(rail)
				
				node.set_next(n, rail)
		

	def __delitem__(self, key):
		return self.remove(key)
	

	def add(self, key, payload, rail = 0, x_node = None):
		node = self.locateNode(key, rail)
		
		if node is None:
			return False
		
		if node.key == key:
			# Already in the list, replace the payload
			node.payload = payload
			
			return True

		n = node.next(rail)
		
		if x_node is None:
			x_node = LLNode( key, payload )
		
		x_node.set_next(n, rail)
		
		node.set_next(x_node, rail)
		
		if rail < self.max_rail:
			if random() * 100 > 50 :
				# promote to the next level
				self.add(key, payload, rail + 1, x_node)

		return True


	def __setitem__(self, key, payload):
		return self.add(key, payload)


	def dump(self, rail = 0):
		print "Rail # %d" % rail
		
		node = self
		
		i = 0

		while True:
			if node.next(rail) is None:
				return

			x = node.next(rail)
			print "%10d %3d %-20s %-20s %s" % ( i, hash(x) % 999, x.key, x.payload, len(x.x_next) )
			
			i += 1
			
			node = node.next(rail)

	logging = False
	
	def log(self, a):
		if self.logging:
			print a

if __name__ == "__main__" :
	levels = 6
	
	max = 10000
	
	ll = LinkList(levels)
	
	for i in xrange(max):
		ll[i] = "Hello %d" % i

	for x in reversed(range(levels)) :
		ll.dump(x)
	
	ll.logging = True
	
	print ll[max / 2]
	
	
if False:
	ll["Niki"]	= "Sofia"
	ll["Alex"]	= "Bourgas"
	ll["Boris"]	= "USSR"
	ll["Zoro"]	= "Mexico"
	ll["Ivan"]	= "Russia"
	ll["John"]	= "USA"
	ll["Mick"]	= "Canada"
	ll["James"]	= "UK"
	ll["Smith"]	= "USA"
	ll["Baron"]	= "Germany"

	#print "Niki" in ll
	#
	#print ll["Niki"]
        #
	#del ll["Niki"]
	#
	#print "Niki" in ll
	#
	#print ll["Niki"]	

	ll.dump(2)
	ll.dump(1)
	ll.dump(0)

	print ll["Niki"]	


