import yagmail
import genera_qr
import genera_utenti

def send(yag,partecipante):
    to = partecipante.email
    subject="Your Crazy Countdown ticket! #TheCrazinessIsBack"
    contents=[yagmail.inline("input/cc2022piena2.png"),f"""
    <html>
    <body style="font-family:Arial; font-size:18px; ">
    <h3>Hi {partecipante.nome} {partecipante.cognome},</h3><h1> TICKET FOR CRAZY COUNTDOWN 2022 - 12TH EDITION!</h1><p style="margin-top:-20px;">The 18th of DECEMBER 2022, is the day of the craziest party of the year!!!</p>
    <h3>TICKET</h3><p style="margin-top:-20px;"><span style="color:red;">To enter the party you have to show the ticket with the QR code that you find attached to this email.</span> At the entrance you will receive the two drinks included in the fee!
    We suggest you to also print the QR code: without QR code it will not be possible to enter the party and each ticket will be validated at the entrance with your ID.
    No ticket will be sold at the entrance.</p>
    <h3>BOTELLON</h3><p style="margin-top:-20px;"><u>Glass bottles are absolutely <b>forbidden</b>.</u> It's not possible to have botellón in front of the disco, the ESN staff will show you the <u><a href="https://goo.gl/maps/yWHXiATuCHEvmD4RA">botellon area</a></u> that will be 100 meters far from the entrance. We suggest you to start your botellon early, around 10:30PM so that you can enter the party on time and don’t miss any moment of this once-in-a-year event!</p>
    <h3>PRICES</h3><p style="margin-top:-20px;">Inside there is a <b>coat room</b>, the cost is 3€ (only coins or cash). Big handbags and backpacks will be required to be stocked at the coat room.
    <span style="color:red;">The cost of extra drinks at the bar is 10€, a beer is 5€.</span></p>
    <h3>TIMINGS and ENTRANCE</h3><p style="margin-top:-20px;"><u>Entrance will be allowed from 11.00 PM to 1.30 AM.
    It is absolutely forbidden to enter with sharp objects, cutlery or pepper sprays; all these objects will be taken by the security at the entrance.</u>
    <u><b>Once inside you can not go out</b></u>, if you go out you can’t enter the party again (there is a smoking area inside). Then at around 3 AM we will make the craziest countdown, all together! The party will end at 4:30 AM.</p>
    <h3>LOCATION</h3><p style="margin-top:-20px;"><span style="color:red;">The party will take place at DISTRETTO INDUSTRIALE 4, in Via Vincenzo Toffetti, 25.</span>
    To reach the DISTRETTO INDUSTRIALE 4 you can take the Yellow Metro (M3) and get down at Porto Di Mare or Corvetto.</p>
    <p>We will be waiting for you for this amazing and unforgettable Crazy Countdown!!!
    See you soon!</p>
    </body>
    </html> """ ]
    genera_qr.make_qr(partecipante)
    attachments="output/qrcode.png"
    yag.send(to,subject,contents,attachments)

def mass_email(partecipanti):
    yag=yagmail.SMTP('cc2022@esnpolimi.it', '9zyvO6Rp^wpbDoJ!/,5W%UFR')
    counter=0
    for partecipante in partecipanti:
        counter=counter+1
        if "@" in partecipante.email: 
            send(yag,partecipante)
            print(f"{counter}/{len(partecipanti)} email sent to {partecipante.email} {partecipante.hash}")
        else:
            print(f"mail invalida {partecipante.email}")
    print("Done!")