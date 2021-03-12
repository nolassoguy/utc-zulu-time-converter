import datetime
import dateutil.parser
import pytz

#3 examples below using the same input for three different timezones

end_time = '2020-08-27T01:00:01.000Z'
dt_UTC = dateutil.parser.parse(end_time)
utc_to_central = dt_UTC.astimezone(pytz.timezone('US/Central'))
central_time = datetime.datetime.strftime(utc_to_central,'%A %B %d, %Y ''@'' %I:%M%p') # Formatting USED TO (changed 1/7/2020) match eBay's "Ended: "
print('CENTRAL: ' + central_time) # CENTRAL: Saturday January 04, 2020 @ 08:00PM

end_time = '2020-08-27T01:00:01.000Z'
dt_UTC = dateutil.parser.parse(end_time)
utc_to_central = dt_UTC.astimezone(pytz.timezone('US/Eastern'))
central_time = datetime.datetime.strftime(utc_to_central,'%A %B %d, %Y ''@'' %I:%M%p') # Formatting USED TO (changed 1/7/2020) match eBay's "Ended: "
print('EASTERN: ' + central_time) # EASTERN: Saturday January 04, 2020 @ 09:00PM

end_time = '2020-08-27T01:00:01.000Z'
dt_UTC = dateutil.parser.parse(end_time)
utc_to_central = dt_UTC.astimezone(pytz.timezone('US/Pacific'))
central_time = datetime.datetime.strftime(utc_to_central,'%A %B %d, %Y ''@'' %I:%M%p') # Formatting USED TO (changed 1/7/2020) match eBay's "Ended: "
print('PACIFIC: ' + central_time) # PACIFIC: Saturday January 04, 2020 @ 06:00PM
