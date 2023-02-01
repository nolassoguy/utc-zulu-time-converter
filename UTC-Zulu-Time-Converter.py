import datetime
import dateutil.parser
import pytz
import re

end_time = input('\nPlease enter a UTC-Zulu Date Time Format (e.g. \'2023-01-30T19:11:05Z\'):\n\n')

# https://www.geeksforgeeks.org/pattern-matching-python-regex/

try:
	zulu_re = re.findall(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$', end_time)[0]

	dt_UTC = dateutil.parser.parse(zulu_re)

	central_time = datetime.datetime.strftime(dt_UTC.astimezone(pytz.timezone('US/Central')),'%A %B %d, %Y ''@'' %I:%M%p') # Formatting USED TO (changed 1/7/2020) match eBay's "Ended: "
	eastern_time = datetime.datetime.strftime(dt_UTC.astimezone(pytz.timezone('US/Eastern')),'%A %B %d, %Y ''@'' %I:%M%p')
	pacific_time = datetime.datetime.strftime(dt_UTC.astimezone(pytz.timezone('US/Pacific')),'%A %B %d, %Y ''@'' %I:%M%p')

	print(f'\nCENTRAL: {central_time}\n\nEASTERN: {eastern_time}\n\nPACIFIC: {pacific_time}\n\n')

except IndexError:
	print('Sorry, that is not in the correct UTC-Zulu Date Time Format')