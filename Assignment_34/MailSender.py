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

def SendMail(SenderMail, AppPassword,ReceiverMail, LogFileName):

    try:

        Message = EmailMessage()

        Message["From"] = SenderMail

        Message["To"] = ReceiverMail

        Message["Subject"] = "Running Process Information Report"

        Body = """

Jay Ganesh...,

The Running Process Information log file has been created successfully.

Please find the attached log file.

Regards,

Sachin Nemaram Patel

"""

        Message.set_content(Body)

        if(os.path.exists(LogFileName) == False):
            return False


        fobj = open(LogFileName, "rb")

        FileData = fobj.read()

        fobj.close()

        FileName = os.path.basename(LogFileName)

        Message.add_attachment(FileData,
                               maintype="application",
                               subtype="octet-stream",
                               filename=FileName)


        SMTPServer = smtplib.SMTP("smtp.gmail.com", 587)

        SMTPServer.starttls()

        SMTPServer.login(SenderMail, AppPassword)

        SMTPServer.send_message(Message)

        SMTPServer.quit()

        return True

    except smtplib.SMTPAuthenticationError:

        return False

    except smtplib.SMTPConnectError:

        return False

    except FileNotFoundError:

        return False

    except PermissionError:

        return False

    except Exception:

        return False