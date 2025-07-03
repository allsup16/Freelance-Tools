import smtplib
import os
import json
from pathlib import Path
from email.message import EmailMessage
from dotenv import load_dotenv    
from datetime import datetime

def today():
    return str(datetime.now().today().date())


load_dotenv()




password = os.getenv('App_Password')

file = "config"

def LoadInstructions(file_name):
    return json.loads(Path(f"{file_name}.json").read_text())

def main():
    instructions = LoadInstructions("config")
    sender = instructions['Sender']
    reciever = instructions['Reciever']
    subject = instructions['Subject']
    message = ''
    if instructions['Message']['Program_Retrieval_List']['Date']==True:
        message += '\n'+today()
    if instructions['Message']['Text']!=None:
        message += instructions['Message']['Text']
    



    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()
    server.login(sender,password)
    server.sendmail(sender,reciever,text) 

main()