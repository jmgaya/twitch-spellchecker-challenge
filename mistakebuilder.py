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
		return self.mistake

	def __toUpperCase(self):
		self.mistake = self.mistake.upper()

	def __addRepeatedVowels(self):
		vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
		self.mistake = re.sub("[aeiouAEIOU]", vowels[random.randint(0,len(vowels)-1)]*random.randint(1,10), self.mistake)

	def __getWord (self):
		with open("/usr/share/dict/words") as f:
			correctWords = f.readlines()
			while (1):
				word = correctWords[random.randint(0, len(correctWords))].rstrip()
				if not word.istitle() and not re.search(r"(.)\1+", word):
					return word