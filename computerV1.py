#!/usr/bin/env python3.6

import sys

from modules.validation import *
from modules.parsing import *
from modules.reduce import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def sqrt(a):
	i = 0
	while (i * i) <= a:
		i += 0.1
	x1 = i
	x2 = i
	j = 0
	while j < 10:
		x2 = a
		x2 /= x1;
		x2 += x1;
		x2 /= 2;
		x1 = x2
		j += 1
	return x2

def solution_c(c):
	if c.cof == 0:
		print("All the real numbers are solution")
	else:
		print("False")

def solution_b(b, c):
	res = -c.cof / b.cof
	if c.cof:
		print("X = -c / b\nX = {0:g} / {1:g} = {3}{2:g}{4}".format(-c.cof, b.cof, res, bcolors.OKGREEN, bcolors.ENDC))
	# if only b
	else:
		print("X = {1}{0:g}{2}".format(res, bcolors.OKGREEN, bcolors.ENDC))

def solution_a(a, b, c):
	if not b:
		b = Polinom("0*X^0")
	if not c:
		c = Polinom("0*X^0")
	# if only a
	if not b and c.cof == 0:
		print("X = 0")
		return
	d = b.cof**2 - (4 * a.cof * c.cof)#b^2 -4ac
	print("Discriminant: = b^2 - 4 * a * c = {1:g} - 4 * {2:g} * {3:g} = {4}{0:g}{5}".format(d, b.cof**2, a.cof, c.cof, bcolors.OKBLUE, bcolors.ENDC))
	print("{1}Discriminant: {0:g}{2}".format(d, bcolors.OKBLUE, bcolors.ENDC))
	if d == 0:
		x = -(b.cof)/(2 * a.cof)
		print("X = -b / (2 * a) = {0:g} / (2 * {1:g}) = {2}{3:g}{4}".format(-(b.cof), a.cof, bcolors.OKGREEN, x, bcolors.ENDC))
		print("{1}The solution is: {0:g} {2}".format(x, bcolors.OKGREEN, bcolors.ENDC))
	elif d > 0:
		print("Discriminant is strictly positive, the two solutions are:")
		x1 = (-(b.cof) - (sqrt(d)))/(2 * a.cof)
		print("{6}1 = (-b - sqrt(d)) / (2 * a) = ({0:g} - ({1:g})) / ({2:g}) = {4}{3:g}{5}".format(-b.cof, sqrt(d), (a.cof), x1, bcolors.OKGREEN, bcolors.ENDC, a.letter))
		x2 = (-(b.cof) + (sqrt(d)))/(2 * a.cof)
		print("{6}2 = (-b + sqrt(d)) / (2 * a) = ({0:g} + ({1:g}) / ({2:g}) = {4}{3:g}{5}".format(-b.cof, sqrt(d), (a.cof), x2, bcolors.OKGREEN, bcolors.ENDC, a.letter))
		print("{2}{4}1: {0:g}\n{4}2: {1:g}{3}".format(x1, x2, bcolors.OKGREEN, bcolors.ENDC, a.letter))
	else:
		print("Discriminant is strictly negative, the two solutions are:")
		x1 = (-(b.cof) - (d**0.5))/(2 * a.cof)
		print("{4}1 = (-b - sqrt(d)) / (2 * a) = ({0:g} - ({1:g})) / ({2:g}) = {3:g}".format(-b.cof, d**0.5, (a.cof), x1, a.letter))
		x2 = (-(b.cof) + (d**0.5))/(2 * a.cof)
		print("{4}2 = (-b + sqrt(d)) / (2 * a) = ({0:g} + ({1:g}) / ({2:g}) = {3:g}".format(-b.cof, d**0.5, (a.cof), x2, a.letter))
		print("{2}{4}1: {0:g}\n{4}2: {1:g}{3}".format(x1, x2, bcolors.OKGREEN, bcolors.ENDC, a.letter))

def solution(exc):
	a = b = c = d = False
	max_degree = 0
	for x in exc:
		if x.degree == 2:
			a = x
		elif x.degree == 1:
			b = x
		elif x.degree == 0:
			c = x
		else:
			d = True
		if max_degree < x.degree:
			max_degree = x.degree
	print("Polynomial degree: {0:g}".format(max_degree))
	if max_degree == 0:
		solution_c(c)
	elif max_degree == 1:
		solution_b(b, c)
	elif max_degree == 2:
		solution_a(a, b, c)
	if max_degree > 2:
		print("The polynomial degree is stricly greater than 2, I can't solve.")


def main():
	line = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 0"
	if len(sys.argv) == 2:
		line = sys.argv[1];
	else:
		print("Frong argv")
		return
	exc = validation(line)
	polinomsLeft, polinomsRight = parsing(exc)

	print('Input:\t\t{0}'.format(line))
	polinoms = reducte(polinomsLeft, polinomsRight) 
	solution(polinoms)
if __name__ == "__main__":
    main()
