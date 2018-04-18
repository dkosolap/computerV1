import re

from modules.validation import *
from modules.parsing import *

def sort(polinoms):
	for i, pol in enumerate(polinoms):
		for j, pol2 in enumerate(polinoms):
			if pol != pol2 and pol.degree < pol2.degree:
				tmp = polinoms[i]
				polinoms[i] = polinoms[j]
				polinoms[j] = tmp
	return polinoms

def reducte(polinomsLeft, polinomsRight):
# Reduct side
	for pol in polinomsLeft:
		for x in polinomsLeft:
			if pol != x and not pol.use and not x.use:
				if pol.degree == x.degree:
					pol.cof += x.cof
					x.use = True
	for pol in polinomsRight:
		for i, x in enumerate(polinomsRight):
			if pol != x and not pol.use and not x.use:
				if pol.degree == x.degree:
					pol.cof += x.cof
					x.use = True
# Del use varrble
	for i, pol in enumerate(polinomsLeft):
		if pol.use:
			del(polinomsLeft[i])
	for i, pol in enumerate(polinomsRight):
		if pol.use:
			del(polinomsRight[i])
# Reduct in one
	for pol in polinomsLeft:
		for x in polinomsRight:
			if not pol.use and not x.use:
				if pol.degree == x.degree:
					pol.cof += -x.cof
					x.use = True
# Del if zero
	for i, x in enumerate(polinomsLeft):
		if x.cof == 0:
			del(polinomsLeft[i])
# Migrate on right
	for x in polinomsRight:
		if not x.use:
			x.cof *= -1
			polinomsLeft.append(x)
# If empty
	if not len(polinomsLeft):
		polinomsLeft.append(Polinom("0*X^0"))
# Sort
	res = sort(polinomsLeft)
	red = ''
	for i, x in enumerate(res):
		if i == 0:
			if x.cof < 0:
				red += '-'
			red += str(x)
		else:
			if x.cof > -1:
				red += " + {0}".format(str(x))
			else:
				red += " - {0}".format(str(x))
	print('Reduced form:\t{0} = 0'.format(red))
	return res