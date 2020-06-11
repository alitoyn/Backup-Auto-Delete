import datetime, os

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

# get months to keep
to_keep = ''
for i in range(month_num + 1 - backlog, month_num + 1):
	if i < 0:
		i += 12
	to_keep += months[i]

	if i != month_num:
		to_keep += '|'


# This command passes the directory through the possibile months so that additional folders are not deleted
# this is then passed through the list of folders to keep
# any folders that make it to the rm command are ones to delete
cmd = 'ls | grep -E "January|February|March|April|May|June|July|August|September|October|November|December" | grep -vE "'+ to_keep +'" | xargs rm -r' 

print(cmd)


# delete old data
