import winsound
from os import system
from time import sleep

def give_options():

	print('\nPlease select a time unit:')
	print('1. Seconds \n2. Minutes \n3. Hours')
	unit = int(input())
	return unit

def play_sound():
	
	for i in range(5):
		winsound.MessageBeep(-1)
		sleep(1)

def alarm(time):

	print(f'\nWait time: {time} seconds')
	sleep(time)
	play_sound()

def take_input(user_unit):
		
		if(user_unit == 1):
			time = int(input('Enter the wait in seconds: '))
			alarm(time)

		elif(user_unit == 2):
			time = int(input('Enter the wait time in minutes: ')) * 60
			alarm(time)

		elif(user_unit == 3):
			time = int(input('Enter the wait time in hours: ')) * 60 * 60
			alarm(time)

		else:
			system('cls')
			main_func()


def main_func():
	unit = give_options()
	take_input(unit)
	return;

main_func()
