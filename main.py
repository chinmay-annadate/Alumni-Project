import wish
import sheet

sender=''
password=''

recipients=sheet.getRecipients()

wish.sendMails(sender,password,recipients)