import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def createMsg(sender,recipient,Alum):
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "WIT Solapur wishes you a very Happy Birthday!"
    msg['From'] = sender
    msg['To'] = recipient

    # Create the body of the message (a plain-text and an HTML version).
    text = """Dear """+Alum+""",\nHere's wishing you tons of happiness on your special day.
    May all your dreams come true and infinite prosperity come your way.\n\nWarm Regards,
    \nWalchand Institute of Technology"""
    
    html = """\
    <html>
        <body style="background: #008888; text-align: center;">

            <img style="padding: 1em;" src="cid:image1" width="550" height="400">
            <h3 style="color: #FFFFFF; padding-left: 1em; padding-right:1em">Dear """+Alum+""",<br>
                Here's wishing you tons of happiness on your special day.<br>
                May all your dreams come true and infinite prosperity come your way.<br><br>
                Warm Regards,<br>
                Walchand Institute of Technology
            </h3><br>
        </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    with open('birthday.jpg', 'rb') as fp:
        msgImage = MIMEImage(fp.read())

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    msg.attach(part1)
    msg.attach(part2)

    return msg.as_string()

def sendMails(sender,password,recipients):
    server = smtplib.SMTP('smtp-mail.outlook.com',587)
    server.starttls()
    server.login(sender,password)
    
    for item in recipients:
        server.sendmail(sender,item['Email Address'],createMsg(sender,item['Email Address'],item['Name']))

    server.quit()

if __name__=='__main__':
    sender=''
    password=''
    recipients=[]
    sendMails(sender,password,recipients)