# Email-Automation

The Quarterly Census of Employment and Wages Program (QCEW) is a Fed-State cooperative program. State Labor Market Information (LMI) agencies prepare and provide quarterly unemployment insurance tax micro data to the U.S. Bureau of Labor Statistics. These data are provided at the establishment level within 15 weeks of receipt.

QCEW Analysts working for the state LMI agencies review data and may contact survey respondents if data is not submitted or if data discrepencies exist. While working as an LMI analyst I created these tools to help automate outreach to respondents. 

## This repository contains:

#### [1] A Bash file that asks the user for the purpose of emailing a respondent. 

#### [2] Two Python files that take user input from the command line, compile an email body based on input, and copies it to the system clipboard to paste into an email client.

* **Standard-Email.py**: This email notifies a respondent of data discrepencies and requests clarification on the change in employment and wages or correction to reported data if it is due to error.

* **Data-Not-Reported.py**: This email notifies a respondent that they have not reported quarterly data and requests the data.

#### [3] An example of the output file that is copied to the system clipboard.

While this code is specific to my work in LMI, it is portable and can be changed to make sending email formats faster.
