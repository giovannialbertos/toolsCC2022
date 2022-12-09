import yagmail
import genera_qr
import genera_utenti

def send(yag,partecipante):
    to = partecipante.email
    subject="Your CrazyCountdown ticket!"
    contents=f"""Hi {partecipante.nome} {partecipante.cognome},
    thank you for signing up for CrazyCountdown! 
    Here is the QR code you'll have to show at the entrance, do not lose it!"""
    genera_qr.make_qr(partecipante)
    attachments="output/qrcode.png"
    yag.send(to,subject,contents,attachments)

def mass_email(partecipanti):
    yag=yagmail.SMTP('cc2022@esnpolimi.it', '9zyvO6Rp^wpbDoJ!/,5W%UFR')
    for partecipante in partecipanti:
        send(yag,partecipante)
        print(f"email sent to {partecipante.email} {partecipante.hash}")
    print("Done!")