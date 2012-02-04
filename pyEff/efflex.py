import sys,re,ply.lex as lex

# Set of keywords in Eiffel
keywords ( 'agent' : 'AGENT',
			'alias' : 'ALIAS',
			'all' : 'ALL',
			'and' : 'AND' ,
			'as'  : 'AS',         
			'assign' : 'ASSIGN',
			'attached' : 'ATTACHED'
			'attribute' : 'ATTRIBUTE' 
			'check' : 'CHECK'
			'class' : 'CLASS'
			'convert' : 'CONVERT'
			'create' : 'CREATE'
			'debug' : 'DEBUG'
			'deferred' : 'DEFERRED'
			'detachable' : 'DETACHABLE'   
			'do' : 'DO' 
	        'else'  : 'ELSE'
	        'elseif' : 'ELSEIF'
  end         ensure     expanded     export       external     feature
  from        frozen     if 	      implies      inherit      inspect
  invariant   like       local 	      loop 	   not 	        note           
  obsolete    old	 once 	      or	   redefine     rename
  require     rescue     retry        select       separate     then
  undefine    until      variant      when 	   xor
)

  
  

