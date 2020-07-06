import random

rollAgain="y"

while (rollAgain=="y"):
	print("\n")
	print ("#" * 10)
	print ("Rolling the dice...")
	print ("You got", random.choice(range(6)))
	print ("#" * 10)

	rollAgain = input("Want to roll the dice again?(y/n): ")