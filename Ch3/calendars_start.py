import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY) # THe Sunday will be as a first day
str = c.formatmonth(2016, 1, 0, 0) # Last two values are indentations values (width, height)
print str

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY) # THe Sunday will be as a first day
str = hc.formatmonth(2016, 1)
print str

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2016, 8):
	print i

# The Calendar module provides useful utilities for the given locale.
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
	print name

for day in calendar.day_name:
	print day

# Calculate days based on a rule: For example, consider 
# a team meeting on the Friday of every month.
# To figure out what days thay would be for each month,
# we can use this script:
for m in range(1, 13):
	# returns an array of weeks that represent the month
	cal = calendar.monthcalendar(2016, m)
	# The first Friday has to be within the first two weeks
	weekone = cal[0]
	weektwo = cal[1]

	# calendar.FRIDAY - return index of Friday in the week. It's 4.
	if weekone[calendar.FRIDAY] != 0:
		meetday = weekone[calendar.FRIDAY]
	else:
		# if the first friday isn't in the first week, it must be in the second
		meetday = weektwo[calendar.  FRIDAY]

# %10 - it's mean insert 10 space before string
print "%10s %3d" % (calendar.month_name[m], meetday)