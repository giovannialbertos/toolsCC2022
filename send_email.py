# import smtplib, ssl

# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "cc2022@esnpolimi.it"  # Enter your address
# receiver_email = "giovannialbertos@hotmail.it"  # Enter receiver address
# #mirko.giovio@esnpolimi.it
# password ="9zyvO6Rp^wpbDoJ!/,5W%UFR"
# message = """\
# Subject: Your CrazyCountdown ticket

# This message is sent from Python."""

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)

import yagmail
yag=yagmail.SMTP('cc2022@esnpolimi.it', '9zyvO6Rp^wpbDoJ!/,5W%UFR')
#sender_email = "cc2022@esnpolimi.it"  # Enter your address
to = "mirko.giovio@esnpolimi.it"
subject="Your CrazyCountdown ticket!"
contents="""Thank you for signing up for CrazyCountdown! 
Here is the QR code you'll have to show at the entrance, do not lose it!"""
attachments="MyQRCode2.png"
yag.send(to,subject,contents,attachments)