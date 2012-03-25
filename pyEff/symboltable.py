class STable():
	def __init__(self):
		self.symbol = {}
	
	def insert(self, lexeme, token):
		if lexeme in self.symbol:
			return False
		else:
			self.symbol[lexeme] = token
			return True
	
	def lookUp(self, lexeme):
		if lexeme in self.symbol:
			return symbol[lexeme]
		else:
			return None


class Scope():
	def __init__(self, par):	# Initializes a scope with parent scope and assigns a separate symbol table to it.
		self.parent = par
		self.table = STable()
	
	def insert(self, token):	# Inserts the token into present scope.
		return self.table.insert(token.lexeme, token)
	
	def lookUp(self, lexeme):	# Make a lookUp for the given lexeme in the present or previous Scopes.
		boundScope = self
		name = None
		while (boundScope != None and name == None):
			name = boundScope.table.lookUp(lexeme)
			boundScope = self.parent
		return name


class Token():
	def __init__(self, lexeme, token):
		self.lexeme = lexeme
		self.type = None
		self.keyword = False
		self.attributes = {}
	
	def __repr__(self):	# To Print
		if self.keyword == False:
			return "Lexeme: " + self.lexeme + " is not a keyword.\n" + "Information- " + "Type: " + self.type + " Attributes: " + self.attributes + "\n"
		else:
			return "Lexeme: " + self.lexeme + " is a keyword.\n" + "Information- " + "Type: " + self.type + " Attributes: " + self.attributes + "\n"