#!/usr/bin/env python3.5
from random import randint
import sys
import os


def clear():

	if os.name == 'nt':

		os.system('cls')

	else:

		os.system('clear')

def questions():

	number = input("How many questions would you like to answer? ")

	try:

		number = int(number)

	except ValueError:

		print("That is not a number!")
		questions()

	difficulty = input("What difficulty do you want? \n"
					   "Easy, Medium, Hard ").lower()

	while True:

		if difficulty == 'easy':

			easy_quiz(number)

		elif difficulty == 'medium':

			medium_quiz(number)

		elif difficulty == 'hard':

			hard_quiz(number)

def easy_quiz(number):

	correct_answers = 0

	while correct_answers < number:

		clear()
		n1 = randint(0, 10)
		n2 = randint(0, 10)
		product = n1 * n2
		answer = int(input("{} * {} = ".format(n1, n2)))

		if answer == product:

			correct_answers += 1
			print("Correct Answer!")

			if correct_answers == number:

				play_again()

			else:

				continue
			
		else:

			print("That was incorrect! The answer was {}".format(product))

def medium_quiz(number):

	correct_answers = 0

	while correct_answers < number:

		n1 = randint(2, 20)
		n2 = randint(2, 20)
		product = n1 * n2
		answer = int(input("{} * {} = ".format(n1, n2)))

		if answer == product:

			correct_answers += 1
			print("Correct Answer!")

			if correct_answers == number:

				play_again()

			else:

				continue
			
		else:

			print("That was incorrect! The answer was {}".format(product))

def hard_quiz(number):

	correct_answers = 0

	while correct_answers < number:

		n1 = randint(5, 35)
		n2 = randint(5, 35)
		product = n1 * n2
		answer = int(input("{} * {} = ".format(n1, n2)))

		if answer == product:

			correct_answers += 1
			print("Correct Answer!")

			if correct_answers == number:

				play_again()

			else:

				continue
			
		else:

			print("That was incorrect! The answer was {}".format(product))

def play_again():

	clear()
	again = input("You did it! Play again? Y/n ")

	if again != 'n':

		questions()

	else:

		print("Thanks for playing!")
		sys.exit()

questions()