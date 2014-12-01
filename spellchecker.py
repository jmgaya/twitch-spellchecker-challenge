#!/usr/bin/python
import sys
import re
import random
from mistakebuilder import *

# ==========================================================
# Not implemented for words containing duplicated consonants
# ==========================================================

class SpellChecker():

	def __init__(self):
		self.wordDictionary = {}	
		self.__fillWordsContainer()

	def showCorrections(self, word):
		self.word = word
		print("> " + word)
		self.__toLowerCase()
		self.__removeRepeatedLetters()
		self.__getCorrections()
		print(self.__getCorrections())

	def __toLowerCase(self):
		self.word = self.word.lower()

	def __removeRepeatedLetters(self):
		self.word = re.sub(r"(.)\1+", r"\1", self.word)

	def __getCorrections (self):
		keyWord = self.__getKeyWord(self.word)
		if (keyWord in self.wordDictionary):
			return self.wordDictionary[keyWord]
		else:
			return "NO SUGGESTION"

	def __fillWordsContainer(self):
		with open("/usr/share/dict/words") as f:
			for word in f.readlines():
				self.__saveWord(word.rstrip())

	def __saveWord(self, word):
		keyWord = self.__getKeyWord(word)
		if (keyWord in self.wordDictionary):
			self.wordDictionary[keyWord].append(word)
		else:
			self.wordDictionary[keyWord] = []
			self.wordDictionary[keyWord].append(word)

	def __getKeyWord(self, word):
		return re.sub("[aeiou]+", "*", word)

if __name__ == "__main__":
	mySpellChecker = SpellChecker()
	mySpellChecker.showCorrections(MistakeBuilder().getMistake())
	