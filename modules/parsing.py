# PARSING = ((?:[+-]?\d+(?:\.\d+)?(?:\*[A-Z])?(?:\^\d+)?)|[+-]?[A-Z](?:\^\d+)?)(?=.*=)
import re

class Polinom(object):
	"""docstring for Polinom"""
	def __init__(self, pol):
		self.cof = float(self.getCof(pol))
		self.degree = int(self.getDegree(pol))
		self.letter = ''
		self.use = False
		if self.degree != 0:
			self.letter = (re.findall(r'[A-Z]', pol))[0]
	def getCof(self, pol):
		check = (re.findall( r'(^(?:[-+])?\d+(?:\.\d+)?)', pol, re.M))
		if len(check) != 0:
			return check[0]
		if len(re.findall( r'(\-)', pol)):
			return -1
		return 1
	def getDegree(self, pol):
		check = (re.findall( r'([A-Z])', pol))
		if len(check):
			check = (re.findall( r'(\^\d+)', pol))
			if len(check):
				return int(re.sub(r'\^', '', check[0]))
			return 1
		return 0 
	def __str__(self):
		res = ""
		if self.degree == 0:
			return "{0:g}".format(abs(self.cof))
		if abs(self.cof) != 1:
			res += '{0:g} * '.format(abs(self.cof))
		res += self.letter
		if self.degree != 1:
			res += "^{0}".format(self.degree)
		return res


		

def parsing(exc):
	left = re.findall( r'((?:[+-]?\d+(?:\.\d+)?(?:\*[A-Z])?(?:\^\d+)?)|[+-]?[A-Z](?:\^\d+)?)(?=.*=)', exc)
	right = re.findall( r'((?:[+-]?\d+(?:\.\d+)?(?:\*[A-Z])?(?:\^\d+)?)|[+-]?[A-Z](?:\^\d+)?)(?!.*=)', exc)
	polinomsLeft = []
	polinomsRight = []
	# print(left)
	# print(right)
	for x in left:
		polinomsLeft.append(Polinom(x))
	for x in right:
		polinomsRight.append(Polinom(x))
	return polinomsLeft, polinomsRight