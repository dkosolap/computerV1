import re

def createError(exc, check):
	res = ("\t{0}\n\t{1}{2}".format(
		exc,
		''.join(str(e) for e in [" " for x in range(check.span()[0])]),
		''.join("^")
		)
	)
	return res

def checkSpace(exc):
	check = re.search( r'\s{2,}', exc)
	if check:
		res = createError(exc, check)
		raise SyntaxError('To many spaces\n' + res)

def checkOperand(exc):
	check = re.search( r'\d \d', exc)
	if check:
		res = createError(exc, check)
		raise SyntaxError("Haven't operator \n" + res)
	check = re.search( r'(?:[\dA-Z](?: )?[A-Z])|(?:[A-Z](?: )?[\dA-Z])', exc)
	if check:
		res = createError(exc, check)
		raise SyntaxError("Haven't operator \n" + res)
	check = re.search( r'[-+*\^/](?: )?[-+\^*/]', exc)
	if check:
		res = createError(exc, check)
		raise SyntaxError("To many operators \n" + res)
	check = re.search( r'[-+*\^/](?: )?[=]', exc)
	if check:
		res = createError(exc, check)
		raise SyntaxError("To many operators \n" + res)
	check = re.search( r'[=](?:.+)?[=]', exc)
	if check:
		res = createError(exc, check)
		raise SyntaxError("To many equals \n" + res)
	check = re.search( r'^=', exc, re.M)
	if check:
		res = createError(exc, check)
		raise SyntaxError("Haven't left side \n" + res)
	check = re.search( r'=$', exc, re.M)
	if check:
		res = createError(exc, check)
		raise SyntaxError("Haven't right side \n" + res)
	check = re.search( r'=', exc)
	if not check:
		check = re.search( r'.$', exc, re.M)
		res = createError(exc, check)
		raise SyntaxError("Haven't equals \n" + res)


def checkSyntax(exc):
	check = re.search( r'[A-Z](?: )?\^\d+\.', exc)
	if check:
		res = createError(exc, check)
		raise SyntaxError("Degree can't be fractional\n" + res)
	check = re.search( r'(?:\.[^\w])|(?:[^\w]\.)', exc)
	if check:
		res = createError(exc, check)
		raise SyntaxError("Lacking number\n" + res)
	check = re.search( r'\d+\.\d\.', exc)
	if check:
		res = createError(exc, check)
		raise SyntaxError("Wrong fractional\n" + res)
	check = re.search( r'\*(?: )?\d(?=\d)', exc)
	if check:
		res = createError(exc, check)
		raise SyntaxError("Unsupported operatoration\n" + res)

def checkLiteral(exc):
	check = re.search( r'[^0-9A-Z+\-*=^.\s]', exc)
	if check:
		res = createError(exc, check)
		raise SyntaxError('Unsupported symbol\n' + res)
	tmp = re.findall( r'[A-Z]', exc);
	if len(tmp) != 0:
		character = (re.search( r'[A-Z]', exc)).group()
		allchar = re.findall(r'[A-Z]', exc)
		for x in allchar:
			if character != x:
				check = re.search(x, exc)
				res = createError(exc, check)
				raise SyntaxError("Another symbol\n" + res)

def validation(exc):
	try:
		if not exc:
			raise SyntaxError('Empty input\n')
		exc = re.sub(r'\s', ' ', exc)
		checkSpace(exc)
		checkSyntax(exc)
		checkOperand(exc)
		checkLiteral(exc)
	except SyntaxError as err:
		print('Syntax Error:\n', err)
		exit()
	return re.sub(r' ', '', exc)






