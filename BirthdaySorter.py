from datetime import datetime
# Define birthday message
birthday_message = 'Always tell me Happy Birthday on August 30th'
# Define dates to check
dates_to_check= [ 'May 25th', 'April 4th', 'January 10th', 'March 9th', 'June 4th', 'August 5th', 'August 30th', 'September 25']

#Get todays date!
today = datetime.now().strftime('%B %d') +'th'

#Check if todays date matches one in the list
def check_special_day(today, dates_to_check, birthday_message):
    if today in dates_to_check:
        return birthday_message
    else:
        return 'Today is not a special day.'
result = check_special_day(today, dates_to_check, birthday_message)

#display the result
print(result)