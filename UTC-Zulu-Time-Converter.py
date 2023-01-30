import datetime
import dateutil.parser
import pytz

end_time = input('\nPlease enter a UTC-Zulu Date Time Format (e.g. \'2023-01-30T19:11:05Z\'):\n\n')

dt_UTC = dateutil.parser.parse(end_time)

utc_to_central = dt_UTC.astimezone(pytz.timezone('US/Central'))
utc_to_eastern = dt_UTC.astimezone(pytz.timezone('US/Eastern'))
utc_to_pacific = dt_UTC.astimezone(pytz.timezone('US/Pacific'))

central_time = datetime.datetime.strftime(utc_to_central,'%A %B %d, %Y ''@'' %I:%M%p') # Formatting USED TO (changed 1/7/2020) match eBay's "Ended: "
eastern_time = datetime.datetime.strftime(utc_to_eastern,'%A %B %d, %Y ''@'' %I:%M%p')
pacific_time = datetime.datetime.strftime(utc_to_pacific,'%A %B %d, %Y ''@'' %I:%M%p')

print(f'\nCENTRAL: {central_time}\n\nEASTERN: {eastern_time}\n\nPACIFIC: {pacific_time}\n\n')