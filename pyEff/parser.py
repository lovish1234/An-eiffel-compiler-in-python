####Parser.py####

import sys
import ply.yacc as yacc
import lexer as lex
from lexer import tokens



class Attribute:
    global MaxPar
    def __init__(self):
            self.id = ""
            self.type = None
            self.isArray = 0    #// True if variable is array
            self.ArrayLimit = 0 # upper limit of array (valid if DIMENSION is true)
            self.width = 0
            self.isPointer = 0
            self.qualifier = 0
            self.specifier = 0
            self.storage = 0
            self.scope = 0
            self.value=None    
            self.isFunction = 0
            self.numParameters = 0
            self.isString = 0
            self.offset = 0
            self.parameterList = [None]*MaxPar


def copyAttribute(a1):      
      i = 0
      a = Attribute()
      a.id=None
      if a1.id != None:
          a.id = a1.id

      a.type=a1.type
      a.isArray=a1.isArray
      a.ArrayLimit=a1.ArrayLimit
      a.width=a1.width
      a.isPointer=a1.isPointer
      a.qualifier=a1.qualifier
      a.specifier=a1.specifier
      a.storage=a1.storage
      a.scope=a1.scope
      a.value=a1.value
      a.isFunction=a1.isFunction
      a.isString=a1.isString
      a.offset=a1.offset
      a.numParameters=a1.numParameters
      #ParameterList      
      for i in range(a1.numParameters):
	    if a1.parameterList[i] == None:
		  break
	    a.parameterList[i] = copyAttribute(a1.parameterList[i])
      return a

def initAttr(a):
      a.id=None
      a.type=None	
      a.isArray=0		# True if variable is array
      a.ArrayLimit=0	#upper limit of array (valid if DIMENSION is true)
      a.width=0
      a.isPointer=0
      a.qualifier=0
      a.specifier=0
      a.storage=0
      a.scope=0
      a.value=None
      a.isString=0
      a.offset=0			#0 means not
      a.numParameters=0
      a.isFunction=0
      for i in range(MaxPar):      
	    a.parameterList[i]=None
      return a
      
      
#>>>>>>> 5c38170289ae94efda4fd09b4ae1f470e1b9e5b6
############################################
#########################################
###########################################
def p_class(p):
	'class : class_header generic_class obsolete_class inheritance create features END'
					###indexing not included yet.
					###obsolete not compulsary and manifest string is yet to be defined for it.

################################################

def p_class_header(p):
	'''class_header : hmark CLASS IDENTIFIER'''

def p_hmark(p):			#SEPERATE not in the statndard format
	'''hmark : DEFERRED
		 | EXPANDED
		 | SEPERATE		
		 | empty'''

#############################################

def p_generic_class(p):
	'''generic_class : LSQUARE generic_list RSQUARE
			 | empty'''

def p_generic_list(p):
	'''generic_list : generic_term
			| generic_list COMMA generic_term
			| empty'''

def p_generic_term(p):
	'''generic_term : IDENTIFIER constraint'''

def p_constraint(p):
	#'''constraint : ARROW class_type
	'''constraint : empty'''		#define ARROW in the lexer file

######################################################

def p_obsolete_class(p):
	'''obsolete_class : OBSOLETE STRING
			  | empty'''

######################################################
#####################################################


def p_inheritance(p):
	'''inheritance : INHERIT inh_list
		       | empty'''

def p_inh_list(p):
	'''inh_list : class_element
		    | inh_list class_element
		    | inh_list COLON class_element'''
		    #| empty'''

def p_class_element(p):
	'''class_element : class_type inh_features'''

def p_inh_features(p):
	'''inh_features : feature_arrangement1
			| feature_arrangement2
			| feature_arrangement3
			| feature_arrangement4
			| feature_arrangement5
			| empty'''
				###not standard in eiffel, but done to make the grammar easier.

#########################################################

def p_feature_arrangement1(p):
	'''feature_arrangement1 : rename export_opt undefine_opt redefine_opt select_opt END'''

def p_feature_arrangement2(p):
	'''feature_arrangement2 : export undefine_opt redefine_opt select_opt END'''

def p_feature_arrangement3(p):
	'''feature_arrangement3 : undefine redefine_opt select_opt END'''

def p_feature_arrangement4(p):
	'''feature_arrangement4 : redefine select_opt END'''

def p_feature_arrangement5(p):
	'''feature_arrangement5 : select END'''

################################################

def p_rename(p):
	'''rename : RENAME rname_list'''

def p_rname_list(p):				###INFIX and PREFIX not present
	'''rname_list : fname ASSIGN fname
		      | rname_list COMMA fname ASSIGN fname'''
		      #| empty'''
 
########################################################

def p_export_opt(p):
	'''export_opt : export
		      | empty'''

def p_export(p):
	'''export : EXPORT elist'''

def p_elist(p):
	'''elist : eitem
		 | elist eitem
		 | elist COMMA eitem'''
		 #| empty'''

def p_eitem(p):
	'''eitem : users routine'''

def p_routine(p):
	'''routine : routine_list
		   | ALL'''

def p_routine_list(p):
	'''routine_list : fname
			| empty'''
		  	#| routine_list COMMA fname'''

##################################################

def p_users(p):
	'''users : LCUR_PARN class_list RCUR_PARN '''

def p_class_list(p):
	'''class_list : IDENTIFIER
		      | class_list COMMA IDENTIFIER
		      | empty'''

#####################################################

def p_undefine_opt(p): 
	'''undefine_opt : undefine
			| empty'''

def p_undefine(p):
	'''undefine : UNDEFINE routine_list'''

def p_redefine_opt(p):
	'''redefine_opt : redefine
			| empty'''

def p_redefine(p):
	'''redefine : REDEFINE routine_list'''

def p_select_opt(p):
	'''select_opt : select 
		      | empty'''

def p_select(p):
	'''select : SELECT routine_list'''

##########################################################
###########################################################

def p_create(p):
	'''create :  create_block
		  | empty'''
					#extend for multiple create block
def p_create_block(p):
	'''create_block : CREATE users_opt proc_list'''

def p_users_opt(p):
	'''users_opt : users
		     | empty'''

def p_proc_list(p):
	'''proc_list : IDENTIFIER
		     | proc_list COMMA IDENTIFIER
		     | empty'''

#####################################################

def p_features(p):
	'''features : fblock
		    | empty'''		#extend for multiple feature blocks

def p_fblock(p):
	'''fblock : FEATURE users_opt fdec_list'''

def p_fdec_list(p):
	'''fdec_list : fdec
		     | fdec_list fdec
		     | fdec_list COLON fdec'''
		     #| empty'''

######################################################

def p_fdec(p):
	'''fdec : new_feature fbody'''

def p_new_feature(p):
	'''new_feature : fname
		       | FROZEN fname'''

def p_fbody(p):
	'''fbody : arg_type_opt basic_body'''

def p_arg_type_opt(p):
	'''arg_type_opt : LPAREN entity_list RPAREN COLON type
		   | empty '''

def p_entity_list(p):
	'''entity_list : entity_group
		       | entity_list entity_group
		       | entity_list COMMA entity_group'''
		       #| empty'''

def p_entity_group(p):
	'''entity_group : idlist COLON type'''

def p_idlist(p):
	'''idlist : IDENTIFIER
		  | idlist COMMA IDENTIFIER'''

######################################################

#def p_type_opt(p):
#	'''type_opt : COLON type
#		    | empty'''

######################################################

def p_basic_body(p):
	'''basic_body : IS fvalue
		      | empty'''

def p_fvalue(p):
	'''fvalue : manifest_constant
		  | UNIQUE
		  | function'''		#manifest_constant not known
					#UNIQUE not defined

#############################3##############################

def p_function(p):
	'''function : function_body END''' 	#Extend for Obsolete
						#Extend for Precondition
						#Extend for Local Variables
						#Extend for Postcondition
						#Extend for Rescue
	
def p_function_body(p):
	'''function_body : DEFERRED
			 | Do fnbody
			 | ONCE fnbody
			 | EXTERNAL STRING exname'''

def p_exname(p):
	'''exname : ALIAS STRING
		  | empty'''

def p_fnbody(p):
	'''fnbody : ins
		  | fnbody ins'''
		  #| empty'''

def p_ins(p):
	'''ins : assignment
	       | conditional
	       | loop
	       | COMMA '''		#Extend for calling a feature
					#Extend for creation of an object
					#Extend for multi branches
					#Extend for debug
					#Extend for check
					#Extend for RETRY

#####################################################################

def p_assignment(p):
	'''assignment : variable ass_op expr'''

def p_variable(p):
	'''variable : IDENTIFIER
		    | RESULT'''


def p_ass_op(p):
	'''ass_op : ASSIGNMENT'''
		  #| REVERSE''' 	#define REVERSE in lexer file if wanted to implement

######################################################

def p_conditional(p):
	'''conditional : IF expr THEN fnbody elseif_group else_opt END'''

def p_elseif_group(p):
	'''elseif_group : elseif_group ELSEIF expr THEN fnbody
			| empty'''
			#| ELSEIF expr THEN fnbody'''

def p_else_opt(p):
	'''else_opt : ELSE fnbody
		    | empty'''

########################################################

def p_loop(p):
	'''loop : FROM fnbody variant UNTIL expr LOOP fnbody END'''

def p_variant(p):
	'''variant : VARIANT
		   | VARIANT expr
		   | VARIANT IDENTIFIER COLON expr
		   | empty'''

###########################################################



#######################################################################
##########Added by Lovish#############################################
######################################################################
	
def p_relexpr(p):
	'''expr : expr EQUAL expr
		| expr NOT_EQUAL expr
		| expr GREATER expr
		| expr LESS expr
		| expr LESS_EQUAL expr
		| expr GREATER_EQUAL expr'''

	if p[2] == '=':
		if p[1].value==p[3].value:
			p[0].value=True
		else:
			p[0].value=False
	elif p[2] == 'NOT_EQUAL':
		if p[1].value!=p[3].value:
			p[0].value=True
		else:
			p[0].value=False
	elif p[2] =='<':
		if p[1].value<p[3].value:
			p[0].value=True
		else:
			p[0].value=False
	elif p[2] =='>':
		if p[1].value>p[3].value:
			p[0].value=True
		else:
			p[0].value=False
	elif p[2] =='LESS_EQUAL' :
		if p[1].value>=p[3].value:
			p[0].value=True
		else:
			p[0].value=False
	elif p[2] =='GREATER_EQUAL':
		if p[1].value<=p[3].value:
			p[0].value=True
		else:
			p[0].value=False
	p[0].type = bool		

			
def p_arithexpr(p):
	'''expr : expr PLUS expr
		| expr MINUS expr
		| expr TIMES expr
		| expr DIVIDE expr
		| expr INT_DIVIDE expr
		| expr INT_REMAINDER expr'''
		#| expr POWER expr'''

	p[0]=Attribute()
	if p[2]=='+':
		p[0].value=p[1].value+p[3].value
		p[0].type = p[1].type
	elif p[2]=='-':
		p[0].value=p[1].value-p[3].value
		p[0].type = p[1].type
	elif p[2]=='*':
		p[0].value=p[1].value*p[3].value
		p[0].type = p[1].type
	elif p[2]=='/':
		p[0].value=p[1].value/p[3].value
		p[0].type = p[1].type
	elif p[2]=='^':
		p[0].value=p[1].value^p[3].value
		p[0].type = p[1].type
	elif p[2]=='//':
		p[0].value=int(p[1].value/p[3].value)
		p[0].type = int	
	elif p[2]=='\\':
		p[0].value=int(p[1].value%p[3].value)	

def p_boolexpr(p):
	'''expr : expr AND expr
		| expr OR expr
		| expr XOR expr
		| expr AND_THEN expr 
		| expr OR_ELSE expr
		| expr IMPLIES expr'''
	p[0]=Attribute()	
	p[0].type=bool	
	if p[2] == 'and' :
		p[0].value=bool(p[1].value and p[3].value)
	elif p[2]=='or':
		p[0].value=bool(p[1].value or p[3].value)	
	elif p[2]=='xor':
		p[0].value=bool((p[1].value and not p[3].value) or (p[3].value and not p[1].value))
	elif p[2]=='and_then':
		if bool(p[1].value)==False:
			p[0].value=False
		else:	
			p[0].value=bool(p[3].value)						
	elif p[2]=='or_else':
		if bool(p[1].value)==True:
			p[0].value=True
		else:	
			p[0].value=bool(p[3].value)
	elif p[2]=='implies':
		if bool(p[1].value)==False:
			p[0].value=True
		else:	
			p[0].value=bool(p[3].value)				
					
def p_expr(p):
	'''expr : RESULT
		| CURRENT
		| LPAREN expr RPAREN
		| bool_const
		| CHARACTER
		| INTEGER
		| REAL
		| STRING'''
		#| BIT
		#| LARRAY expr_list RARRAY 
		#| NOT expr
		#| FREEOP expr 
		#| expr FREEOP expr
		
		#| OLD expr
		#| STRIP '(' attr_list ')' '''
		
                
#=======
#		| expr IMPLIES expr
#		| OLD expr
#		| STRIP '(' attr_list ')' '''

#>>>>>>> 5c38170289ae94efda4fd09b4ae1f470e1b9e5b6
def p_attr_list(p):
	'''attr_list : IDENTIFIER
		     | attr_list COMMA IDENTIFIER
		     | empty'''

def p_expr_list(p):
	'''expr_list : expr
		     | expr_list COMMA expr
		     | empty'''


def p_manifest_constant(p):
	'''manifest_constant : bool_const
		    	     | CHARACTER
		    	     | int_const
		    	     | real_const
		             | STRING'''
		    	     #| BIT'''	#define BIT type in the lexer file

		#Note: Does not support 'Wide_character_constant'.
		#Note: Does not support 'Wide_manifest_string'.
		#Note: Does not support 'Hexadecimal_constant'.

def p_bool_const(p):
	'''bool_const : TRUE
		      | FALSE'''

def p_int_const(p):
	'''int_const : INTEGER
		     | MINUS INTEGER %prec UMINUS
		     | PLUS INTEGER %prec UPLUS'''


def p_real_const(p):
	'''real_const : REAL
		      | MINUS REAL %prec UMINUS
		      | PLUS REAL %prec UPLUS'''
	

#######################################################
######################################################

def p_fname(p):
	'''fname : IDENTIFIER'''
		 #| PREFIX STRING
		 #| INFIX STRING'''		#INFIX and PREFIX not yet defined, they can be made optional.
					#valid INFIX and PREFIX operators can be checked by the manifest string.

###################################################

def p_type(p):
	'''type : class_type
		| EXPANDED class_type
		| LIKE CURRENT
		| LIKE IDENTIFIER'''
		#| SEPARATE class_type
		#| BITTYPE int_constant
		#| BITTYPE IDENTIFIER'''		#integer_constant yet to be defined
						#BITTYPE yet to be identified

def p_class_type(p):
	'''class_type : IDENTIFIER generic'''

def p_generic(p):
	'''generic : LSQUARE type_list RSQUARE
		   | empty'''

def p_type_list(p):
	'''type_list : type
		     | type_list COMMA type
		     | empty'''
	
def p_empty(p):
	'empty :'
	pass

def p_error(p):
    print("Syntax error at '%s'" % p.value)

precedence = (
	('left', 'IMPLIES'),
	('left', 'OR', 'OR_ELSE', 'XOR'),
	('left', 'AND', 'AND_THEN'),
	('left', 'EQUAL','NOT_EQUAL','GREATER','LESS','LESS_EQUAL','GREATER_EQUAL'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE', 'INT_DIVIDE', 'INT_REMAINDER'),
#	('right', 'POWER'),
	('right', 'UPLUS', 'UMINUS', 'NOT'),            # Unary minus operator
	
)

yacc.yacc()

