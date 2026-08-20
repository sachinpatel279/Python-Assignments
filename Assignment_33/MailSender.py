########################################################
#
# File Name : MailSender.py
# Description : Send Log File Through Email
# Author : Sachin Nemaram Patel
#
########################################################

import smtplib
import os
from email.message import EmailMessage
########################################################
#
# Function Name : SendMail
#
########################################################

def SendMail(SenderMail, AppPassword, ReceiverMail, LogFileName, StartTime, EndTime, DirectoryName, TotalFiles, DuplicateFound, DuplicateDeleted):

    try:

        Message = EmailMessage()

        Message["From"] = SenderMail

        Message["To"] = ReceiverMail

        Message["Subject"] = "Duplicate File Removal Report"

        Body = f"""

Jay Ganesh,

The duplicate-file removal operation has been completed successfully.

Operation Statistics

Starting time of scanning : {StartTime}

Completion time of scanning : {EndTime}

Directory scanned : {DirectoryName}

Total number of files scanned : {TotalFiles}

Total number of duplicate files found : {DuplicateFound}

Total number of duplicate files deleted : {DuplicateDeleted}

Regards,

Marvellous Automation System

Please find the detailed log file attached to this email.

"""

        Message.set_content(Body)

        if(os.path.exists(LogFileName) == False):

            return False

        fobj = open(LogFileName,"rb")

        FileData = fobj.read()

        fobj.close()

        FileName = os.path.basename(LogFileName)

        Message.add_attachment(FileData,
                               maintype="application",
                               subtype="octet-stream",
                               filename=FileName)

        SMTPServer = smtplib.SMTP("smtp.gmail.com",587)

        SMTPServer.starttls()

        SMTPServer.login(SenderMail,AppPassword)

        SMTPServer.send_message(Message)

        SMTPServer.quit()

        return True
    
    except smtplib.SMTPException:

        return False

    except FileNotFoundError:

        return False

    except PermissionError:

        return False

    except Exception:

        return False