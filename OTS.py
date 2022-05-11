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
# Your Phone Number for Notification
your_phone     = REPLACEME7
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
#define function to shortly flash the logo in the beginning of the program
def bling():
    print(Fore.RED + rise + Style.RESET_ALL)
    time.sleep(0.01)
    print(clear)
    time.sleep(0.02)
    print(Style.DIM + rise + Style.RESET_ALL)
    time.sleep(0.01)
    print(clear)
    time.sleep(0.01)

#defining internet connection checking function
def check_connection():
    url='http://www.google.com/'
    timeout=5
    checkloop = True
    while checkloop == True:
           try:
                  server     = smtplib.SMTP('smtp.gmail.com', 587)
                  _ = requests.get(url, timeout=timeout)
                  print(clear +  Fore.LIGHTGREEN_EX)
                  print(connection)
                  time.sleep(0.5)
                  print(""+Style.RESET_ALL)
                  print(clear)
                  checkloop = False
           except requests.ConnectionError:
                  print(clear + Fore.LIGHTRED_EX)
                  print(noconnection)
                  time.sleep(2)
                  print(""+Style.RESET_ALL)
                  print("ConnectionError.")
                  input("Enter to try again...")
           except smtplib.SMTPConnectError:
                  print(clear + Fore.LIGHTRED_EX)
                  print(noconnection)
                  time.sleep(2)
                  print(""+Style.RESET_ALL)
                  print("SMTPConnectError.")
                  input("Enter to try again...")

#defining email function to confirm check-ins to operator
def gmail_send(subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, pw)
    msg            = EmailMessage()
    message        = f'{message}\n'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From']    = fromaddr
    msg['To']      = destaddr
    server.send_message(msg)

#defining check in collection function, recording last 3 check ins
def check_in():
    run = True
    while run == True:
        if M41.upper() == "M":
            del last3check[0]
            last3check.append("Mcheck")
        elif M41.upper() == "C":
            del last3check[0]
            last3check.append("Ccheck")

############################################################################################### P R O G R A M        S T A R T #############################################################################################################
check_connection()
while Set == False:
    while Set1 == False:
        print(clear)
        print("           CURRENT OPERATION: "+OPERATION)
        print("           CORRECT? (y/n)")
        CONF = input("           ---> ")
        if   CONF.upper() == "N":
            print(clear)
            print("""
           --  ENTER OPERATION NAME --
                                 """)
            choice = input("OPERATION ")
            print("")
            OPERATION = choice.upper()
            for line in fileinput.FileInput("var.py", inplace=1):
                if "OPERATION      = " in line:
                    line = line.replace(line, "OPERATION      = '"+str(OPERATION)+"'\n")
                print(line, end='')
            print(clear)
        elif CONF.upper() == "Y":
            Set1 = True
        else:
            continue
    while Set2 == False:
        print(clear)
        print("           CURRENT OVERWATCH: "+OVERWATCH)
        print("           CORRECT? (y/n)")
        CONF = input("           ---> ")
        if   CONF.upper() == "N":
            print(clear)
            print("""
           -- ENTER OVERWATCH PHONE --
                                 """)
            choice = input("OVERWATCH PHONE NR : ")
            print("")
            OVERWATCH = choice.upper()
            for line in fileinput.FileInput("var.py", inplace=1):
                if "OVERWATCH      = " in line:
                    line = line.replace(line, "OVERWATCH      = '"+str(OVERWATCH)+"'\n")
                print(line, end='')
            print(clear)
        elif CONF.upper() == "Y":
            Set2 = True
        else:
            continue
    if "ngrok.exe" in (p.name() for p in psutil.process_iter()):
        print(Fore.GREEN+"NGROK ALREADY RUNNING"+Style.RESET_ALL)
        time.sleep(0.5)
    else:
        os.startfile("NGROK.lnk")
    while Set3 == False:
        print(clear)
        print("           CURRENT NGROK URL: "+URL)
        print("           CORRECT? (y/n)")
        CONF = input("           ---> ")
        if   CONF.upper() == "N":
            print(clear)
            print("""
           --    ENTER NGROK URL   --
                                 """)
            choice = input("           http://")
            print("")
            URL = "http://"+choice
            for line in fileinput.FileInput("var.py", inplace=1):
                if "URL            = " in line:
                    line = line.replace(line, "URL            = '"+str(URL)+"'\n")
                print(line, end='')
            print(clear)
        elif CONF.upper() == "Y":
            Set3 = True
        else:
            continue
    while Set4 == False:
        print(clear)
        if   timeT == FOURhours:
            x = "4h"
        elif timeT == THREEhours:
            x = "3h"
        elif timeT == TWOhours:
            x = "2h"
        elif timeT == ONEhour:
            x = "1h"
        elif timeT == test:
            x = "3min (test)"
        print("           CURRENT TIME T: "+x)
        print("           CORRECT? (y/n)")
        CONF = input("           ---> ")
        if   CONF.upper() == "N":
            print(clear)
            print("""
           -- CHOOSE T TIME WINDOW  --
                    (1) 1h
                    (2) 2h
                    (3) 3h
                    (4) 4h
                    (T) 3 minutes (test)

                       """)
            choice = input("")
            if   choice == "1":
                timeT = '1:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeT          = " in line:
                        line = line.replace(line, "timeT          = '"+str(timeT)+"'\n")
                    print(line, end='')
            elif choice == "2":
                timeT = '2:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeT          = " in line:
                        line = line.replace(line, "timeT          = '"+str(timeT)+"'\n")
                    print(line, end='')
            elif choice == "3":
                timeT = '3:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeT          = " in line:
                        line = line.replace(line, "timeT          = '"+str(timeT)+"'\n")
                    print(line, end='')
            elif choice == "4":
                timeT = '4:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeT          = " in line:
                        line = line.replace(line, "timeT          = '"+str(timeT)+"'\n")
                    print(line, end='')
            elif choice.upper() == "T":
                timeT = '0:03:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeT          = " in line:
                        line = line.replace(line, "timeT          = '"+str(timeT)+"'\n")
                    print(line, end='')
            print(clear)
        elif CONF.upper() == "Y":
            Set4 = True
            break #why is this necessary????
        else:
            continue
    while Set5 == False:
        print(clear)
        if   timeC == FOURhours:
            x = "4h"
        elif timeC == THREEhours:
            x = "3h"
        elif timeC == TWOhours:
            x = "2h"
        elif timeC == ONEhour:
            x = "1h"
        elif timeC == test:
            x = "3min (test)"
        print("           CURRENT TIME C: "+x)
        print("           CORRECT? (y/n)")
        CONF = input("           ---> ")
        if   CONF.upper() == "N":
            print(clear)
            print("""
           -- CHOOSE C TIME WINDOW  --
                    (1) 1h
                    (2) 2h
                    (3) 3h
                    (4) 4h
                    (T) 3 minutes (test)

                       """)
            choice = input("")
            if   choice == "1":
                timeC = '1:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeC          = " in line:
                        line = line.replace(line, "timeC          = '"+str(timeC)+"'\n")
                    print(line, end='')
            elif choice == "2":
                timeC = '2:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeC          = " in line:
                        line = line.replace(line, "timeC          = '"+str(timeC)+"'\n")
                    print(line, end='')
            elif choice == "3":
                timeC = '3:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeC          = " in line:
                        line = line.replace(line, "timeC          = '"+str(timeC)+"'\n")
                    print(line, end='')
            elif choice == "4":
                timeC = '4:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeC          = " in line:
                        line = line.replace(line, "timeC          = '"+str(timeC)+"'\n")
                    print(line, end='')
            elif choice.upper() == "T":
                timeC = '0:03:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeC          = " in line:
                        line = line.replace(line, "timeC          = '"+str(timeC)+"'\n")
                    print(line, end='')
            print(clear)
        elif CONF.upper() == "Y":
            Set5 = True
            break #why is this necessary????
        else:
            continue
    while Set6 == False:
        print(clear)
        x = mode
        print("           CURRENT MODE: "+x)
        print("           CORRECT? (y/n)")
        CONF = input("           ---> ")
        if   CONF.upper() == "N":
            print(clear)
            print("""               --
           --    CHOOSE OTS MODE    --
                    (1) HOT
                    (2) TEST
                       """)
            choice = input("")
            if   choice == "1":
                mode = "HOT"
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "mode           = " in line:
                        line = line.replace(line, "mode           = '"+str("HOT")+"'\n")
                    print(line, end='')
                MODE = Fore.LIGHTRED_EX+"                    HOT HOT HOT"+Style.RESET_ALL
            elif choice == "2":
                mode = "TEST"
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "mode           = " in line:
                        line = line.replace(line, "mode           = '"+str("TEST")+"'\n")
                    print(line, end='')
                MODE = Fore.GREEN      +"                    TEST TEST TEST"+Style.RESET_ALL
            print(clear)
        elif CONF.upper() == "Y":
            if mode == "HOT":
                MODE = Fore.LIGHTRED_EX+"                    HOT HOT HOT"+Style.RESET_ALL
            elif mode == "TEST":
                MODE = Fore.GREEN      +"                    TEST TEST TEST"+Style.RESET_ALL
            Set6 = True
            break #why is this necessary? is it?
        else:
            continue
    SET = False
    while SET == False:
        print(clear)
        if   timeT == "4:00:00":
            timeT = datetime.timedelta(hours=4)
            TTT   = "4 hours"
        elif timeT == "3:00:00":
            timeT = datetime.timedelta(hours=3)
            TTT = "3 hours"
        elif timeT == "2:00:00":
            timeT = datetime.timedelta(hours=2)
            TTT = "2 hours"
        elif timeT == "1:00:00":
            timeT = datetime.timedelta(hours=1)
            TTT = "1 hour"
        elif timeT == "0:03:00":
            timeT = datetime.timedelta(minutes=3)
            TTT = "3 minutes (test)"
        if   timeC == "4:00:00":
            timeC = datetime.timedelta(hours=4)
            CCC = "4 hours"
        elif timeC == "3:00:00":
            timeC = datetime.timedelta(hours=3)
            CCC = "3 hours"
        elif timeC == "2:00:00":
            timeC = datetime.timedelta(hours=2)
            CCC = "2 hours"
        elif timeC == "1:00:00":
            timeC = datetime.timedelta(hours=1)
            CCC = "1 hour"
        elif timeC == "0:03:00":
            timeC = datetime.timedelta(minutes=3)
            CCC = "3 minutes (test)"
        print("""

  Operative Travel Security System
  --      current settings      --

      OPERATION """+Fore.LIGHTGREEN_EX+OPERATION+Style.RESET_ALL+          """
   OVERWATCH     = """+Fore.LIGHTGREEN_EX+str(OVERWATCH)+Style.RESET_ALL+  """
   NGROK URL     = """+Fore.LIGHTGREEN_EX+str(URL)+Style.RESET_ALL+        """
   T TIME WINDOW = """+Fore.LIGHTGREEN_EX+str(TTT)+Style.RESET_ALL+        """
   C TIME WINDOW = """+Fore.LIGHTGREEN_EX+str(CCC)+Style.RESET_ALL+        """
   MODE          = """+                   mode                    +        """


        (1) START OTS | RERUN SETTINGS (2)"""+Style.RESET_ALL)
        CONF = input("           ---> ")
        if   CONF.upper() == "1":
            print(clear)
            print("")
            SET = True
            Set = True
        elif CONF.upper() == "2":
            Set  = False
            Set1 = False
            Set2 = False
            Set3 = False
            Set4 = False
            Set5 = False
            SET  = True
            break #why is this necessary????
        else:
            continue

#Set Mode Part 1
if mode == "HOT":
    COPS   = "+4930110"      #Police Germany
    FOROFF = "+493018172000" #Foreign Office Germany
elif mode == "TEST":
    COPS   = your_phone
    FOROFF = your_phone 

#Set Mode Part 2
while run == False:
        print(clear)
        print("""
           [1] TIMEMODE   |   CHECKMODE [2]
                                 """)
        choice = input("           ---> ")
        if choice == "1":
                TIMEMODE  = True
                run       = True
        elif choice == "2":
                CHECKMODE = True
                run       = True
        else:
                print(Fore.LIGHTRED_EX+"INVALID"+Style.RESET_ALL)
                time.sleep(1)

#do bling() with max of 7 times
run = True
while run == True:
    bling()
    c += 1
    if c == 7:
        run = False
# OTS
while OTS == True:
    if TIMEMODE == True:################################################################################################################################################################################################# TIMEMODE
        timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
        timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
        runningT = True
        while runningT == True:
            print(clear)
            now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
            now = str(now)
            print("           >--- "+Fore.LIGHTRED_EX+"O"+Fore.RED+"perative "+Fore.LIGHTRED_EX+"T"+Fore.RED+"ravel "+Fore.LIGHTRED_EX+"S"+Fore.RED+"ecurity System "+Style.RESET_ALL+"---< ("+Style.BRIGHT+"5.0"+Style.RESET_ALL+")"+Fore.RED)
            print("                    OPERATION "+Fore.LIGHTRED_EX+OPERATION.upper()+Style.RESET_ALL)
            print(MODE)
            print("                    "+now)
            print("                    TIME MODE ("+TTT+")")
            if   ALPHA == True:
                    print(Fore.LIGHTYELLOW_EX+"                    ALPHA ALPHA ALPHA"+Style.RESET_ALL)
            elif ALPHA == False:
                    print("")
            timerNOW     = datetime.datetime.now().strftime("%H:%M:%S, %m/%d/%Y")
            timerNOW     = datetime.datetime.strptime(timerNOW, "%H:%M:%S, %m/%d/%Y")
            DELTA        = timerNOW - timerSTART
            if   TTT == "4 hours":
                if DELTA.seconds >= 10800 and DELTA.seconds < 14400:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 14400:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            elif TTT == "3 hours":
                if DELTA.seconds >= 7200 and DELTA.seconds < 10800:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 10800:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            elif TTT == "2 hours":
                if DELTA.seconds >= 5400 and DELTA.seconds < 7200:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 7200:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            elif TTT == "1 hour":
                if DELTA.seconds >= 2700 and DELTA.seconds < 3600:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 3600:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            elif TTT == "3 minutes (test)":
                if DELTA.seconds >= 120 and DELTA.seconds < 180:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 180:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
            now = str(now)
            if os.path.exists(REPORTTIME) == False:
                report = open(REPORTTIME, 'w')
                report.write(now + " TIME STARTED!")
                report.close()
            if DELTA < timeT:
                emails   = True
                messages = True
                REACHED  = False
                LoggedIn = False
                while LoggedIn == False:
                    now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                    now = str(now)
                    try:
                        mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
                        mail.login(fromaddr, pw)
                        LoggedIn = True
                    except (imaplib.IMAP4.error, imaplib.IMAP4.abort,ConnectionResetError):
                        print(Fore.LIGHTRED_EX + "LOGIN FAILED" + Style.RESET_ALL)
                        if os.path.exists("ERRORLOG.txt") == False:
                                report = open("ERRORLOG.txt", 'w')
                                report.write(now + " LOGINERROR")
                                report.close()
                        elif os.path.exists("ERRORLOG.txt") == True:
                                report = open("ERRORLOG.txt", 'a')
                                report.write("\n" + now + " LOGINERROR")
                                report.close()
                listloop = True
                while listloop == True:
                    try:
                        mail.list()
                        mail.select("inbox")
                        listloop = False
                    except:
                        print("ERROR (mail.list)")
                result, data   = mail.search(None, 'SUBJECT "[OTS]"')
                result2, data2 = mail.search(None, 'FROM "noreply@findmespot.com"')
                ids  = data[0]
                ids2 = data2[0]
                id_list  = ids.split()
                id_list += ids2.split()
                try:
                        latest_email_id = id_list[-1]
                        messages = True
                except IndexError:
                        now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                        now = str(now)
                        print(clear)
                        print("           >--- "+Fore.LIGHTRED_EX+"O"+Fore.RED+"perative "+Fore.LIGHTRED_EX+"T"+Fore.RED+"ravel "+Fore.LIGHTRED_EX+"S"+Fore.RED+"ecurity System "+Style.RESET_ALL+"---< ("+Style.BRIGHT+"5.0"+Style.RESET_ALL+")"+Fore.RED)
                        print("                    OPERATION "+Fore.LIGHTRED_EX+OPERATION.upper()+Style.RESET_ALL)
                        print()
                        print("                    "+now)
                        print("                    TIME MODE")
                        print()
                        messages     = False
                        timerNOW     = datetime.datetime.now().strftime("%H:%M:%S, %m/%d/%Y")
                        timerNOW     = datetime.datetime.strptime(timerNOW, "%H:%M:%S, %m/%d/%Y")
                        DELTA        = timerNOW - timerSTART
                        if   TTT == "4 hours":
                                if DELTA.seconds >= 10800 and DELTA.seconds < 14400:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 14400:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        elif TTT == "3 hours":
                                if DELTA.seconds >= 7200 and DELTA.seconds < 10800:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 10800:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        elif TTT == "2 hours":
                                if DELTA.seconds >= 5400 and DELTA.seconds < 7200:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 7200:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        elif TTT == "1 hour":
                                if DELTA.seconds >= 2700 and DELTA.seconds < 3600:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 3600:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        elif TTT == "3 minutes (test)":
                                if DELTA.seconds >= 120 and DELTA.seconds < 180:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 180:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        print("Waiting for Check-In (" + str(missedCount) + " missed)")
                        time.sleep(1)
                if messages == True:
                    def empty_folder(m, do_expunge=True):
                        print(Fore.LIGHTGREEN_EX + "CHECKED IN! " + Style.RESET_ALL + Fore.GREEN + now + Style.RESET_ALL)
                        REACHED = True  #############################################################################################################
                        m.select("inbox")  # select all trash
                        m.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
                        if do_expunge:  # See Gmail Settings -> Forwarding and POP/IMAP -> Auto-Expunge
                            m.expunge()  # not need if auto-expunge enabled
                        else:
                            print("Expunge was skipped.")
                            return
                    result, data = mail.fetch(latest_email_id, "RFC822")
                    m = mailparser.parse_from_bytes(data[0][1])
                    text = "From: "  # the Signature of emails sent by my phone. After that, anything is irrelevant
                    entry = m.body.split(text, 1)[0]
                    message = str(entry.upper())
                    empty_folder(mail)
                    now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                    now = str(now)
                    if "CHECK" in message:
                            timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
                            timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
                            if ALPHA == True:
                                ALPHA = False
                                if "(" in message and ")" in message:
                                    coordinates = re.findall(regex,message)
                                    coordinates = str(coordinates)
                                else:
                                    coordinates = "[no coordinates]"
                                check = "Alpha End("+now+" "+coordinates+")"
                                del last3check[0]
                                last3check.append(check)
                                gmail_send("CONFIRMATION","ALPHA END. "+str(last3check)+" -41")
                            elif ALPHA == False:
                                if "(" in message and ")" in message:
                                    coordinates = re.findall(regex,message)
                                    coordinates = str(coordinates)
                                else:
                                    coordinates = "[no coordinates]"
                                check = "Check In("+now+" "+coordinates+")"
                                del last3check[0]
                                last3check.append(check)
                                gmail_send("CONFIRMATION","CHECK IN CONFIRMED. "+str(last3check)+" -41") 
                            if os.path.exists(REPORTTIME) == False:
                                    report = open(REPORTTIME, 'w')
                                    report.write(now + " CHECKED IN! "+coordinates)
                                    report.close()
                            elif os.path.exists(REPORTTIME) == True:
                                    report = open(REPORTTIME, 'a')
                                    report.write("\n" + now + " CHECKED IN! "+coordinates)
                                    report.close()
                            missedCount = 0
                    elif "FLIGHT" in message:  # Flight Mode
                        print(now + Fore.LIGHTRED_EX + " FLIGHT MODE ACTIVATED." + Style.RESET_ALL)
                        if "(" in message and ")" in message:
                            coordinates = re.findall(regex,message)
                            coordinates = str(coordinates)
                        else:
                            coordinates = "[no coordinates]"
                        check = "Flight Start("+now+" "+coordinates+")"
                        del last3check[0]
                        last3check.append(check)
                        gmail_send("CONFIRMATION","FLIGHT MODE ACTIVATED. "+str(last3check)+" -41")
                        time.sleep(0.1)
                        message = client.messages.create(
                                to     = OVERWATCH,
                                from_  = 