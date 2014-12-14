import sys
import re
import random

class MistakeBuilder():

	def __init__(self):
		self.wordDictionary = {}
		self.mistake = self.__getWord()
		print(self.mistake)

	def getMistake(self):
		self.__toUpperCase()
		self.__addRepeatedVowels()
		self.__addRepeatedConsonants()
		return self.mistake

	def __toUpperCase(self):
		self.mistake = self.mistake.upper()

	def __addRepeatedVowels(self):
		self.mistake = re.sub("[AEIOU]", self.__repeatLetter, self.mistake)

	def __addRepeatedConsonants(self):
		self.mistake = re.sub("[B-DF-HJ-NP-TV-Z]", self.__repeatLetter, self.mistake)

	def __repeatLetter(self, matchobj):
		return matchobj.group(0)*random.randint(1,10)

	def __getWord (self):
		with open("/usr/share/dict/words") as f:
			correctWords = f.readlines()
			while (1):
				word = correctWords[random.randint(0, len(correctWords))].rstrip()
				if not word.istitle() and not re.search(r"(.)\1+", word):
					return word