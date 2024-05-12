
# Online Python - IDE, Editor, Compiler, Interpreter
# importing datetime, pytz modules
from datetime import datetime
import pytz
MIN_MEETING_HOUR = datetime(year=2024, month=5, day=12, hour=2, minute=58, second=39)
MAX_MEETING_HOUR = datetime(year=2024, month=5, day=13, hour=1,minute=58, second=39)
def organize_meeting(utcTimeZone, localTimeZone):
    # Getting the local timezone
    localTimeZone = pytz.timezone('CET')
    # Getting the UTC timeZone
    utcTimeZone = datetime.now(pytz.utc)
    # format string
    format = '%Y:%m:%d %H:%M:%S %Z %z'
    # Convert the time to the local timezone
    local = utcTimeZone.astimezone(localTimeZone)
    local_min = MIN_MEETING_HOUR.astimezone(localTimeZone)
    local_max = MAX_MEETING_HOUR.astimezone(localTimeZone)
    # Getting formatted time using strftime() function
    print("Formatted DateTime in Local Timezone : ",local.strftime(format))
    print("Formatted DateTime in UTC Timezone : ",utcTimeZone.strftime(format))
    print("Formatted MaximumTime:  ", MAX_MEETING_HOUR.strftime(format))
    print("Formatted MinimumTime:  ", MIN_MEETING_HOUR.strftime(format))
    difference = int(local.strftime('%z'))
    print(difference)
    difference2 = int(utcTimeZone.strftime('%z'))
    print(difference2)
    local_min = int(local_min.strftime('%z'))
    print(local_min)
    local_max = int(local_max.strftime('%z'))
    print(local_max)
    # Comparing Time Zones
    if (difference > difference2):
       print('UTC TimeZone is behind the Local Timezone by',local.strftime('%z'),'Hours')
    if(difference < difference2):
       print('UTC TimeZone is ahead of the Local TimeZone by',utcTimeZone.strftime('%z'),'Hours')
    print(difference2 - local_min)
    print(difference - local_max)
    if((difference-local_min) and (difference-local_max) == 0):
        return True
    else:
        return False

localTimeZone = pytz.timezone('CET')
utcTimeZone = datetime.now(pytz.utc)
print(organize_meeting(localTimeZone, utcTimeZone))
     
