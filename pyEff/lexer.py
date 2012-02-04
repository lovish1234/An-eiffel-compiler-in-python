# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
Keywords = {
	'and':'AND',
	'or':'OR',
	'true':'TRUE',
	'false':'FALSE',
	'not':'NOT',
	'xor':'XOR',
	'implies':'IMPLIES',
	'if':'IF',
	'then':'THEN',
	'else':'ELSE',
	'elseif':'ELSEIF',
	'inspect':'INSPECT',
	'when':'WHEN',
	'loop':'LOOP',
	'until':'FROM',
	'class':'CLASS',
	'creation':'CREATION',
	'do':'Do',
	'end':'END',
	'expanded':'EXPANDED',
	'feature':'FEATURE',
	'indexing':'INDEXING',
	'is':'IS',
	'like':'LIKE',
	'local':'LOCAL',
	'current':'CURRENT',
	'check':'CHECK',
	'require':'REQUIRE',
	'ensure':'ENSURE',
	'variant':'VARIANT',
	'invariant':'INVARIANT',
		#added
	'agent' : 'AGENT',
	'alias' : 'ALIAS',
	'all' : 'ALL',
	'as' : 'ASSIGN',
	'attached' : 'ATTACHED',
	'attribute' : 'ATTRIBUTE',
	#'check' : 'CHECK',
	'create' : 'CREATE',
	'convert' : 'CONVERT',
	'debug' : 'DEBUG' ,
	'deferred' : 'DEFERRED',
	'detachable' :'DETACHABLE',
	#'ensure' : 'ENSURE',
	#'expanded' : 'EXPANDED',
	'export' : 'EXPORT',
	'external' : 'EXTERNAL',
	'frozen' : 'FROZEN' ,
	'implies' : 'IMPLIES',
	'inherit' : 'INHERIT',
	'inspect' : 'INSPECT',
	'loop' : 'LOOP',
	'note' : 'NOTE',
	'obsolete' : 'OBSOLETE',
	'old' : 'OLD',
	'once' : 'ONCE',
	'redefine' : 'REDEFINE',
	'rename' : 'RENAME',
	'resque' : 'RETRY',
	'select' : 'SELECT',
	'seperate' : 'SEPERATE',
	'undefine' : 'UNDEFINE',
	
}
tokens =  [
   'INTEGER',
   'REAL',
   'CHARACTER',
   'BOOLEAN',
   'ARRAY',
   'PLUS',
   'MINUS',
   'TIMES',
   'INT_REMAINDER',
   'DIVIDE',
   'INT_DIVIDE',
   'GREATER',
   'GREATER_EQUAL',
   'LESS',
   'LESS_EQUAL',
   'EQUAL',
   'NOT_EQUAL',
   'AND_THEN',
   'OR_ELSE',
   'ASSIGNMENT',
   'SEPARTOR',
   'LPAREN',
   'RPAREN',
   'IDENTIFIER',
   'COMMENT',
   #added
   #'BOOL',
   'DOT',
   'DQUOTES',
]+ list(Keywords.values())





# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_INT_REMAINDER  = r'\\'
t_INT_DIVIDE  = r'//'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUAL = r'='
t_ASSIGNMENT = r':='
t_LESS = r'<'
t_GREATER = r'>'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_SEPARTOR = r';'
#added
t_DOT = r'.'
t_DQUOTES = r'"'


# A regular expression rule with some action code

def t_COMMENT(t):
    r'[-][-][^\n]+'
    pass
def t_REAL(t):
    r'[\d]*(\.\d*)([e|E](\+|\-)?\d+)?'
    #r'[\d]+(\.\d+)([e|E](\+|\-)?\d+)?'
    return t    
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t
def t_OR_ELSE(t):
    r'or\selse'
    t.value = str(t.value)    
    return t
def t_AND_THEN(t):
    r'and\sthen'
    t.value = str(t.value)    
    return t
#def t_CHARACTER(t):
 #   r'[a-zA-Z]'
  #  t.value = str(t.value)    
   # return t
def t_BOOL(t):
	r'[true|false|TRUE|FALSE]'
	t.value=bool(t.value)
def t_IDENTIFIER(t):
    r'[a-zA-Z]\w*'
    t.type= Keywords.get(t.value,'IDENTIFIER')    # Check for reserved words   
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
--3<= 3and d_ sdd3= + 4 and or or or else
--10-- 
--true
--true TRUE FALSE lovish
NEGETIVE = -567
REAL = 3.14159265358979323846 ""
--  + -20 or 2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok
