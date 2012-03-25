# ------------------------------------------------------------
# lexer.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
Keywords = {
	'and':'AND',
	'arrow' : 'ARROW',
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
	'until': 'UNTIL',
	'from': 'FROM',
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
	'reverse' : 'REVERSE',
	'resque' : 'RETRY',
	'result' : 'RESULT',
	'select' : 'SELECT',
	'seperate' : 'SEPERATE',
	'undefine' : 'UNDEFINE',
	'unique' : 'UNIQUE',

}
tokens =  [
   'POWER'
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
   'BOOL',
   'COLON',
   'DOT',
   'LCUR_PARN',
   'RCUR_PARN',
   'LSQUARE',
   'RSQUARE',
   'DQUOTES',
   'HEXINT',
   'OCTINT',
   'CHARCONST',
   'BININT',
   'STRING',
   'COMMA',
   'AT_SIGN'
]+ list(Keywords.values())



#string type required for "Hello , World " in this programe
def t_STRING(t):
	r'[\"][^\"]+[\"]'
	t.value=str(t.value)
	return t
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
#Correction done
t_ASSIGNMENT = r'\:='
t_LESS = r'<'
t_GREATER = r'>'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_SEPARTOR = r';'
#added
t_DOT = r'\.'
t_DQUOTES = r'"'
t_COLON =r'\:'
t_LCUR_PARN=r'\{'
t_RCUR_PARN=r'\}'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_COMMA = r'\,'
t_AT_SIGN = r'\@'
# A regular expression rule with some action code

def t_COMMENT(t):
    r'[-][-][^\n]+'
    pass

def t_CHARCONST(t):
	r'[\'][%][ABCDHFLNQRSTUV\%\'\"\)\(\<\>][\']'
	t.value=str(t.value)
	return t   
def t_HEXINT (t) :
	r'[0][xX][0-9a-fA-F]+'
	t.value=str(t.value)
	return t 
def t_OCTINT(t):
	r'[0][cC][0-7]+'
	t.value=str(t.value)
	return t
#BININT needs to be corrected	
def t_BININT(t):
	r'[0][bB][01]+'
	t.value=str(t.value)
	return t	
def t_REAL(t):
    r'[\d]+(\.)\d*([e|E](\+|\-)?\d+)?  | [\d]+([e|E](\+|\-)?\d+) | [\d]*(\.)\d+([e|E](\+|\-)?\d+)?'
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
def t_CHARACTER(t):
    r'[\'][a-zA-Z][\']'
    t.value = str(t.value)    
    return t

def t_BOOL(t):
    r'[\s][true|false|TRUE|FALSE][\s]'
    t.value= bool(t.value)
    print t
    pass	
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
##data = '''
##--3<= 3and d_ sdd3= + 4 and or or or else
##--10-- 
##true true TRUE FALSE lovish
##--VROOM = 0B1101
##--'a'
##--'%A'
##--ROOM = 0c32434
##--BOOM = 0xabc234
##--NEGETIVE = -567
##--REAL = 3.14159265358979323846 ""
##--  + -20 or 2
##VROOM = 0B1001
##class
##  	  HELLO
##  create
##    	  make
##  feature
##	  make
##		do
##			io.put_string ("Hello, world! %N ")
##			io.put_new_line
##                end
##  end
## 
##'''
data = '''
1.
1.2
.2
.2e4
1.2e4
1e4
1
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok
