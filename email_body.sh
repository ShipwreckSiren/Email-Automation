#!/bin/bash

cd "C:\cygwin64\home\a_user\bin"

echo "What type of email are you sending? Edit Failure (EF), No Data Reported (NDR), or Coding Info Request (CIR)?"
read -p "Email type: " emailtype

if [[ $emailtype = 'EF' ]]
then 
	python Standard-Email.py

else
	python Data-Not-Reported.py

fi

wait

echo "$(< body.txt)"

chmod 711 email_body.sh
