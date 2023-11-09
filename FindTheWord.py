import pyperclip
import random

def findletter(letters):
	
	# Open a file a retrieve the text
	with open('words_file.txt', 'r') as file:
		words_file = file.read().splitlines()

	# Find the words that have the letters

	# Initialize an empty list to hold the text
	matching_words = []

	# Go through each word in the dictionary
	for word in words_file:
		# If the letters are in the word, add the word to the list
		if letters in word:
			matching_words.append(word)

	return matching_words

while True:

	# User input & send to function
	letters = input("Enter the letters or write (exit): ")

	if letters == "exit":
		print("Coded by 0xn4if, thanks for using!")
		break

	# Sending the letter to function
	matching_words = findletter(letters)

	print(f"Words containg '{letters}': ")
	for word in matching_words:
		print(word)

	# Select random output
	randomOutput = random.choice(matching_words)
	print(f"\nWe get random choice for you: '{randomOutput}' it has been copied in the clipboard")
	pyperclip.copy(randomOutput)



