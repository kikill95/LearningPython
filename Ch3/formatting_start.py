from datetime import datetime

def main():
	# Times and Dates can be formatted using a set of predefined string
	# control codes
	now = datetime.now() # get the current date and time

	#### Date formating ####

	# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
	print now.strftime("%Y") # full year with the century(2016)
	print now.strftime("%y") # full year without the century(16)
	print now.strftime("%a, %d %B, %y") # abbreviated day, num, full month, abbreviated year

	# %c - locale's date and time, %x - locale's date, %X - locale's time
	print now.strftime("%c")
	print now.strftime("%x")
	print now.strftime("%X")

	#### Time Formating ####

	# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
	print now.strftime("%I:%M:%S %p") # 12-Hour:Minute:Second:AM
	print now.strftime("%H:%M") # 24-Hour:Minute



if __name__ == '__main__':
	main();