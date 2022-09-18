import wish
import sheet
import os

sender=os.environ['ALUMNI_UNAME']
password=os.environ['ALUMNI_PASS']

recipients=sheet.getRecipients()

wish.sendMails(sender,password,recipients)