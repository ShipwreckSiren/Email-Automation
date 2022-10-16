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

chg_type = input("Employment failure, Wage failure, or both? Type E, W, or B: ").upper()
if chg_type == 'E':
    emp_wgs = 'employment'
elif chg_type == 'W':
        emp_wgs = 'wages'
else: 
    emp_wgs = 'employment and wages'

incr_decr = input("Did it increase or decrease? Type I or D: ").upper()
if incr_decr == 'I':
    direc = 'an increase'
    econ_chg = "(acquisition, expansion, new worksite or contract, etc)"
    direc2 = 'increase'
else:
    direc = 'a decrease'
    econ_chg = "(less business, end of project or loss of contract, layoff, closure, etc)"
    direc2 = 'decrease'

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

    first_half = '{}\n\nI am emailing in regards to an unemployment insurance account for {} (Acct#: {}). This account was flagged in our system for review due to {} in reported {} during quarter {} of 20{}. In order to notate the account with any important economic changes {}, could you provide an explanation for the {} in reported {}? '.format (msg, comp_name, acct_num, direc, emp_wgs, qtr, yr, econ_chg, direc2, emp_wgs)

    second_half = ' \n\nThank you for your time and do reach out if you have any questions or concerns.\n\n'

    if add_info == 'N':
        body = first_half + second_half
    if add_info == 'Y':
        body = first_half + '\n\n' + xtra_info + second_half

    return body

body = message(add_info,xtra_info)

path = r'C:\cygwin64\home\a_user\bin'
file = 'body.txt'
dir_list = os.listdir(path)

with open(os.path.join(path, file), 'w') as fp: 
    fp.write(body) 

pyperclip.copy(body)
