#Symbol Table



class symbolTable:
class HashTable:
	def __init__(self):
		self.hashtable = {}

	def lookup(self, symbol):
		try:
			 return self.hashtable(hashFunction(symbol))
		except:
			return None

	def insert(self, symbol, value):
		key = hashFunction(symbol)
		self.hashtable[key] = [symbol, value]

	def hashFunction(symbol):
		return hashValue

class Node:
	def __init__(self):
		self.childParent = None
		self.childCount = 0
		self.childArray = []
		self.sT = symbolTable()

def createNewChild(Node):
	childNode = Node()
	childNode.childParent = Node
	Node.childCount++
	Node.childArrary.append(childNode)
	return childNode

def insertSymbol(Node, symbol, value):
	Node.st.insert(symbol, value)

def lookupSymbol(Node, symbol):
	Node.st.lookup(symbol)
