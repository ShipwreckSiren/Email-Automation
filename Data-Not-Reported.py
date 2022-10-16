##############################################################################
# Gather User Input, Compile Text Based on Input, and Copy Text to Clipboard #
##############################################################################

import datetime
from datetime import date
import os
import pytz
import pyperclip

####################
# Assign Variables #
####################

comp_name = input("Enter Company Name: ")
acct_num = input("Enter Account Number: ")
qtr = input("Enter quarter (1-4): ")
yr = input("Enter year (last 2 digits): ")

qtr_ordinal = ' '.join(['first' if qtr == '1' else 'second' if qtr == '2'
            else 'third' if qtr == '3' else 'four'])

add_info = input("Would you like to ask more information about the change in employment and/or wages? Y or N: ").upper()
if add_info == 'Y':
    xtra_info = input("Add supplementary information regarding change(s) in employment and/or wages: ")
if add_info == 'N':
    xtra_info = ''


#currentTime = datetime.datetime.now()
#currentTime.hour
#ct = currentTime.strftime("%H:%M")

mountain = pytz.timezone('America/Denver')
currentTime = (datetime.datetime.now(tz=mountain))

if currentTime.hour < 12:
    msg = "Good morning," 
elif 12 <= currentTime.hour < 18:
    msg = "Good afternoon," 
else:
    msg = "Good evening,"

###########################
# Define Message Function #
###########################

def message(add_info,xtra_info):

    first_half = '{}\n\nI am emailing in regards to a Colorado SUI account for {} (Acct#: {}).\n\nWe have not received a quarterly report for the {} quarter of 20{}. Could you kindly forward your monthly employment numbers, total quarterly wages, and total taxable wages so that I can enter the account data into our system?'.format (msg, comp_name, acct_num, qtr_ordinal, yr)

    second_half = ' \n\nThank you for your time and do reach out if you have any questions or concerns.\n\n'

    if add_info == 'N':
        body = first_half + second_half
    if add_info == 'Y':
        body = first_half + xtra_info + second_half

    return body

body = message(add_info,xtra_info)

path = r'C:\cygwin64\home\a_user\bin'
file = 'body.txt'
dir_list = os.listdir(path)

with open(os.path.join(path, file), 'w') as fp: 
    fp.write(body) 

pyperclip.copy(body)
