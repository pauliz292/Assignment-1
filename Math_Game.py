import random
import time
from operator import itemgetter

class Math_Game(object):
	"""docstring for Math_Game"""
	def Main(self):
		self.__init__()

	def __init__(self):
		self.username = 'Guest'
		self.corrects = 0
		self.errors = 0
		self.questionAnswer = 0
		self.userAnswer = 0
		self.operation = random.randint(0,3)
		self.firstNum = random.randint(1,99)
		self.secondNum = random.randint(1,99)
		self.starttime = 0
		self.endtime = 0

	def LogIn(self, username):
		self.username = ''
		self.username = input("Username: ")

	def CheckAnswer(self, corrects, errors):
		if(self.userAnswer == self.questionAnswer):
			print("Your answer is CORRECT!")
			self.corrects += 1
		else:
			print("Your answer is WRONG!")
			self.errors += 1

	def RandomizeValues(self):
		self.operation = random.randint(0,3)
		self.firstNum = random.randint(1,99)
		self.secondNum = random.randint(1,99)

	def AnswerSheet(self, answer):
		self.userAnswer = float(input("Answer: "))

	def ShowResults(self):
		self.result = str({
			'Username:': self.username,
			'Time:': self.endtime,
			'Score:': self.corrects,
			'Errors:': self.errors
			})
		try:
			self.resultFile = open('Results.txt','a')
			self.resultFile.write(self.result)
			self.resultFile = open('Results.txt','r')
			print(self.resultFile.readlines())
		finally:
			self.resultFile.close()

	def GameLoop(self):
		while(self.corrects < 10 and self.errors < 10):
			self.starttime = time.time()
			self.RandomizeValues()
			#addition
			if(self.operation == 0):
				self.questionAnswer = self.firstNum + self.secondNum
				print("What is {} {} {}?".format(self.firstNum, "+", self.secondNum))
				self.AnswerSheet(self.userAnswer)
				self.CheckAnswer(self.corrects, self.errors)
			#subtraction
			elif(self.operation == 1):
				if(self.firstNum > self.secondNum):
					self.questionAnswer = self.firstNum - self.secondNum
					print("What is {} {} {}?".format(self.firstNum, "-", self.secondNum))
					self.AnswerSheet(self.userAnswer)
					self.CheckAnswer(self.corrects, self.errors)
				else:
					self.RandomizeValues()
			#multiplication
			elif(self.operation == 2):
				if(self.firstNum or self.secondNum != 1):
					self.questionAnswer = self.firstNum * self.secondNum
					print("What is {} {} {}?".format(self.firstNum, "x", self.secondNum))
					self.AnswerSheet(self.userAnswer)
					self.CheckAnswer(self.corrects, self.errors)
				else:
					self.RandomizeValues()
			#division
			elif(self.operation == 3):
				if(self.firstNum or self.secondNum != 1 and self.firstNum < self.secondNum):
					self.questionAnswer = self.firstNum / self.secondNum
					print("What is {} {} {}?".format(self.firstNum, "/", self.secondNum))
					self.AnswerSheet(self.userAnswer)
					self.CheckAnswer(self.corrects, self.errors)
				else:
					self.RandomizeValues()
		self.endtime = time.time() - self.starttime
		self.EndGame()

	def math_game(self):
		#Start game
		#setup game
		while(self.username):
			self.LogIn('')
			if(self.username != ''):
				self.loginQuestion = input("Do you want to start game {} (y/n)?".format(self.username))
				if(self.loginQuestion == "y"):
					self.corrects = 0
					self.errors = 0
					self.GameLoop()
				else:
					self.EndGame()
			else:
				self.EndGame()

	def EndGame(self):
		print("Thanks for playing!")
		self.ShowResults()






game = Math_Game()
game.math_game()

		
		
