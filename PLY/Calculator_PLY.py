import ply.lex as lex

#the token list : all the possible tokens
tokens = ('PLUS','MINUS','TIMES','DIVIDE','NUMBER','LPAR','RPAR')


#Each token has a match declaration of the form t_TOKENNAME
#Tokens must define with regular expression
t_ignore = '\t'
t_PLUS   = r'\+'
t_MINUS  = r'\-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
#we used : instead of EQUALS
# t_EQUALS = r'='
t_LPAR   = r'\('
t_RPAR   = r'\)'
# t_NAME   = r'[a-zA-Z_][a-zA-Z0-9_]*' in case we wanted add names

#functions are used for special course of actions that must be done!
def t_NUMBER(t):
  r'\d+'#docstring hold regular exp.
  t.value = int(t.value)
  return t
  
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

#build the lexer by creating a master regular expressions
lex.lex() #build the lexer

#Grammer rules incoded as function with names p_rulename
#names doesnt matter as long as start with p_

def p_s(p):
	'S : E'
	p[0] = p[1]

def p_ep(p):
	'E : E PLUS T'
	p[0] = p[1] + p[3]

def p_em(p):
	'E : E MINUS T'
	p[0] = p[1] + p[3]

def p_et(p):
	'E : T'
	p[0] = p[1]

def p_tm(p):
	'T : T TIMES F'
	p[0] = p[1] * p[3]

def p_td(p):
	'T : T DIVIDE F'
	p[0] = p[1] / p[3]

def p_tf(p):
	'T : F'
	p[0] = p[1]

def p_fa(p):
	'F : NUMBER'
	p[0] = p[1]
	print (p[0])

def p_fp(p):
	'E : LPAR E RPAR'
	p[0] = p[1]+p[2]+p[3]
	
	
def p_fan(p):
	'F : MINUS NUMBER'
	p[0] = -p[2]
	print (p[0])

def p_fpn(p):
	'E : MINUS LPAR E RPAR'
	p[0] = -p[2]+p[3]+p[4]


def p_error(p):
  print("Syntax error at '%s'" % p.value)


#after all, creating the parser
import ply.yacc as yacc
yacc.yacc()

while True:
  s = str(input('Calculator > '))
  if s.strip()=='':
	  break
  yacc.parse(s)
