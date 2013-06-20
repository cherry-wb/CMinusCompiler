import ply.yacc as yacc
from cminus_lexer import tokens
import cminus_lexer
import sys



def p_program(p):
	'program : declaration_list'
	pass

def p_declaration_list_1(p):
	'declaration_list : declaration_list declaration'
	#p[0]dd = p[1] + p[2]  # DUDA
	pass

def p_declaration_list_2(p):
	'declaration_list : declaration'
	pass
 
 
def p_declaration(p):
	'''declaration : var_declaration
				  | fun_declaration
				  '''
	pass

def p_fun_declaration(p):
	'fun_declaration : type_specifier ID LPAREN params RPAREN compount_stmt'
	pass
    
def p_var_declaration_1(p):
	'var_declaration : type_specifier var_declaration2 SEMICOLON'
	pass

#definicion de  los tipos de datos
def p_var_declaration_2(p):
	'var_declaration : type_specifier ID LBRACKET NUMBER RBRACKET SEMICOLON'
	pass

#Declaracion a,b,c etc
def p_var_declaration_3(p):                     
	'''var_declaration2 : ID COMMA var_declaration2    
	                               | ID 
	                               | COMMA'''
	pass
                                     

def p_type_specifier(p):
	'''type_specifier : INT
					| VOID
					| CHAR
					| LONG
					| FLOAT
					| DOUBLE
					| SIGNED
					| SHORT'''
	pass


def p_params(p):
	'''params : param_list
			| VOID
			| empty'''
	pass	

def p_param_list_1(p):
	'''param_list : param_list COMMA param
				| param'''
	pass

def p_param(p):
	'''param : type_specifier ID
			| type_specifier ID LBRACKET RBRACKET'''
	pass

def p_compount_stmt(p):
	'''compount_stmt : LBLOCK local_declarations statement_list RBLOCK
					| LBLOCK statement_list RBLOCK'''
	pass

def p_local_declarations(p):
	'''local_declarations : local_declarations var_declaration
						| empty'''
	pass

def p_statement_list(p):
	'''statement_list : statement_list statement
					| empty'''
	pass

def p_statement_2(p):
	'''statement2 : expression_stmt
				| compount_stmt
				| selection_stmt
				| iteration_stmt
				| return_stmt
	'''
	pass

#mas cosas dentro de un if
def p_statement(p):    
        '''statement : statement statement2     
                       | statement2
                        '''
pass

def p_expression_stmt(p):        
	'''expression_stmt : expression terminacion
					| SEMICOLON
					| DOSPUNTOS
					| expression_stmt expression terminacion'''
	pass

def p_terminacion(p):            #a,b,c
	'''terminacion : terminacion terminacion2
	                  | terminacion2'''
	                 
	pass

def p_terminacion_2(p):  
	'''terminacion2 : SEMICOLON
	                 | DOSPUNTOS'''
	pass

                            

def p_selection_stmt_2(p):
	'selection_stmt : IF LPAREN expression RPAREN statement ELSE statement'  
	pass

def p_selection_stmt_3(p):   
	'selection_stmt : IF LPAREN expression RPAREN LBLOCK statement RBLOCK '   
	pass


def p_selection_stmt_4(p):   
	'selection_stmt : IF LPAREN expression RPAREN LBLOCK statement RBLOCK ELSE LBLOCK statement RBLOCK '   
	pass

def p_selection_stmt_5(p):
	'selection_stmt : IF LPAREN expression RPAREN statement'
	pass

def p_selection_stmt_6(p):   
	'selection_stmt : IF LPAREN expression RPAREN LBLOCK statement RBLOCK ELSE statement  '   
	pass

def p_iteration_stmt(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN statement'
	pass

def p_iteration_stmt_2(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN LBLOCK statement RBLOCK'
	pass

def p_for(p):
	'iteration_stmt : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN' 
	pass

def p_do(p):
	'iteration_stmt : DO LBLOCK statement RBLOCK WHILE LPAREN expression RPAREN SEMICOLON' 
	pass

def p_return_stmt(p):
	'''return_stmt : RETURN SEMICOLON
				| RETURN expression SEMICOLON'''
	pass

def p_expression(p):
	'''expression : var EQUAL expression
				| simple_expression'''
	pass
 
def p_var(p):
	'''var : ID
		| ID LBRACKET expression RBRACKET'''
	pass

def p_simple_expression(p):
	'''simple_expression : additive_expression relop additive_expression
						| additive_expression '''
	pass


def p_relop(p):
	'''relop : LESS 
			| LESSEQUAL
			| GREATER
			| GREATEREQUAL
			| DEQUAL
			| DISTINT
	'''
	pass

#se definen expresiones a + b, a-b, a +1, 1+2,
def p_additive_expression(p):
	'''additive_expression : ID addop ID
						| ID addop NUMBER
						| NUMBER addop ID
						| NUMBER addop NUMBER
						| ID
						| NUMBER
						| ID PLUS PLUS
						| ID MINUS MINUS
						| ID PLUS EQUAL ID
						| ID PLUS EQUAL NUMBER
						| PLUS PLUS ID
						| ID TIMES EQUAL NUMBER
						| ID TIMES EQUAL ID'''
	
	                          
	pass

def p_addop(p):
	'''addop : PLUS 
	    	| MINUS
	       	| GREATER
	        | GREATEREQUAL
		  	| DEQUAL
		  	| DISTINT
		  	| TIMES
		  	| DIVIDE
	'''
	pass



def p_empty(p):
	'empty :'
	pass


def p_error(p):
	#print str(dir(p))
	#print str(dir(cminus_lexer))
	if p is not None:
		print "tienes un error de sintaxis en la linea: " + str(p.lexer.lineno) + " Unexpected token  " + str(p.value)
	else:
		print "tienes un error de sintaxis en la linea: " + str(cminus_lexer.lexer.lineno)

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'examples/evaluacion.c'

	f = open(fin, 'r')
	data = f.read()
	print data
	parser.parse(data, tracking=True)
	

