import datetime

# import data from config
from config import *

# init needed variables
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# work out if deleteing months or years
# ^ this should be set in the config file


# get current date
date = datetime.datetime.now()
month_num = int(date.month) - 1
# month_num = 11 		# use this to test different months

# convert to words
# print(months[month_num])

# get months to delete
for i in range(month_num - backlog, month_num):
	if i < 0:
		i += 12

	print(months[i])


# delete old data
