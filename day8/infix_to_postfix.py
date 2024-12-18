infix_expr = input('Enter the infix notation expression: ')

i               = 0
stk             = ''
postfix_expr    = ''
present_char    = ''
operator        = ''

for char in infix_expr:
	if i == len(infix_expr):
		break
	if i == 0:
		stk = infix_expr[i]
		i += 1
	else:
		stk = postfix_expr
		postfix_expr = ''
	operator = infix_expr[i]
	i += 1
	present_char = infix_expr[i]
	i += 1
	postfix_expr = stk + present_char + operator
	stk = ''
	present_char = ''
	operator = ''

print(f'Postfix Expression = {postfix_expr}')