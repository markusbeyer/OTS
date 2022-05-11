import time, os, sys, datetime, smtplib, imaplib, mailparser, requests, fileinput, psutil, re
from colorama                    import *
from email.mime.text             import *
from twilio.rest                 import Client
from email.message               import EmailMessage
from var                         import OPERATION, OVERWATCH, CHECKPOINTS, URL, timeT, timeC, mode
init()
################################################################################################################# OTS ######################################################################################################################
#                                                                                                          V A R I A B L E S
clear          = "\033[2J\033[1;1f"
now            = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
now            = str(now)
missedCount    = 0
c              = 0
regex          = re.compile(".*?\((.*?)\)")
test           = "0:03:00"
ONEhour        = "1:00:00"
TWOhours       = "2:00:00"
THREEhours     = "3:00:00"
FOURhours      = "4:00:00"
SIXhours       = "6:00:00"
REPORTTIME     = "reportTIME.txt"
REPORTCHECK    = "reportCHECK.txt"
timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
timerNOW       = datetime.datetime.now().strftime("%H:%M:%S, %m/%d/%Y")
timerNOW       = datetime.datetime.strptime(timerNOW, "%H:%M:%S, %m/%d/%Y")
DELTA          = timerNOW - timerSTART
last3check     = ["NEWSTART","NEWSTART","NEWSTART"]
# FPackage Password
Fpassword      = REPLACEME1
# ACCOUNT CREDS FOR GMAIL AND TWILIO FOR EMAIL AND SMS NOTIFICATION
fromaddr       = REPLACEME2
pw             = REPLACEME3
destaddr       = REPLACEME4
server         = smtplib.SMTP('smtp.gmail.com', 587) #gmail  server
ACCOUNT        = REPLACEME5
TOKEN          = REPLACEME6
client         = Client(ACCOUNT,TOKEN)               #twilio client
# OTS PARAMETER VARS
OTS            = True
runningT       = True
runningC       = True
nochecks       = True
CHECKMODE      = False
TIMEMODE       = False
pending        = False
ALPHA          = False
SWITCH         = False
LoggedIn       = False
Set            = False
Set1           = False
Set2           = False
Set3           = False
Set4           = False
Set5           = False
Set6           = False
SET            = False
run            = False
rise = """
                    X
                   XX
                  XXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXX
                 XX
                 X

  
                XXXXX
              XXX  XXX
             XXX     X
              XXXX
              XXXXXX
          XXXXXXXXXXXXXXX"""
#No connection pic
noconnection ="""
       XXX               XXX
        XXX             XXX  
         XXX           XXX  
          XXX         XXX
           XXX       XXX
            XXX     XXX
             XXX   XXX
              XXX XXX
               XXXXX
               XXXXX
              XXX XXX
             XXX   XXX
            XXX     XXX
           XXX       XXX
          XXX         XXX
         XXX           XXX
        XXX             XXX
       XXX               XXX
  - N O    C O N N E C T I O N -"""
#Connection pic
connection ="""
                                VVV  
                               VVV  
                              VVV
                             VVV
                            VVV
                           VVV
                          VVV
                         VVV
        VVV             VVV
         VVV           VVV 
          VVV         VVV 
           VVV       VVV    
            VVV     VVV      
             VVV   VVV       
              VVVVVVV
               VVVVV
                VVV            
                 V

  -      C O N N E C T E D      -"""
################################################################################################################# OTS ######################################################################################################################
#                                                                                                          F U N C T I O N S
