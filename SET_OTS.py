import time, fileinput
from colorama import *
init()
clear = "\033[2J\033[1;1f"

print("WELCOME TO OTS")
time.sleep(1)
print("Before using, we need to take care of some settings.")
time.sleep(1)
input("ENTER TO PROCEED")

print(clear)

#add info/presentation
print("SET PASSWORD FOR F PACKAGE")
time.sleep(1)
password = input("ENTER PASSWORD: ")
password = "'"+password+"'"

print(clear)

print("SET GMAIL FOR NOTIFICATIONS")
time.sleep(1)
email_from = input("ENTER GMAIL: ")
email_from = "'"+email_from+"'"

print(clear)

print("SET GMAIL PASSWORD")
time.sleep(1)
email_pw = input("ENTER GMAIL PASSWORD: ")
email_pw = "'"+email_pw+"'"

print(clear)

print("SET NOTIFICATIONS DESTINATION EMAIL ADDRESS")
time.sleep(1)
email_dest = input("ENTER DEST EMAIL: ")
email_dest = "'"+email_dest+"'"

print(clear)

print("SET TWILIO ACCOUNT")
time.sleep(1)
twilio_account = input("ENTER TWILIO ACCOUNT: ")
twilio_account = "'"+twilio_account+"'"

print(clear)

print("SET TWILIO TOKEN")
time.sleep(1)
twilio_token = input("ENTER TWILIO TOKEN: ")
twilio_token = "'"+twilio_token+"'"

print(clear)

print("SET YOUR PHONE NUMBER")
time.sleep(1)
your_phone = input("ENTER YOUR PHONE NUMBER: ")
your_phone = "'"+your_phone+"'"

print(clear)

print("Feeding changes to OTS...")
time.sleep(1)

def replace(search_text, new_text):
    with fileinput.input("OTS.py", inplace=True) as file:
        for line in file:
            new_line = line.replace(search_text, new_text)
            print(new_line, end='')

replace("REPLACEME1",password)
replace("REPLACEME2",email_from)
replace("REPLACEME3",email_pw)
replace("REPLACEME4",email_dest)
replace("REPLACEME5",twilio_account)
replace("REPLACEME6",twilio_token)
replace("REPLACEME7",your_phone)

print("ALL IS DONE!")
time.sleep(1)
print(clear)
print("YOU MAY NOW USE OTS!")
time.sleep(1)
print(clear)
print("RERUN THIS IF NEEDED")
time.sleep(1)
print(clear)
print("BYE!")
time.sleep(1)



