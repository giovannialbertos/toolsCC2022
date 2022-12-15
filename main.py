import genera_utenti
import genera_qr
import send_email
import sys

if len(sys.argv)<2:
    partecipanti=genera_utenti.get_partecipanti("input/partecipanti_prova.csv")
if len(sys.argv)>2:
    print("too many arguments, input only the file name")
    quit()
else:
    partecipanti=genera_utenti.get_partecipanti(sys.argv[1])
    genera_utenti.print_partecipanti(partecipanti)
genera_utenti.generate_SQL_dump(partecipanti)
print("Partecipanti caricati su DB? (yes per continuare, invio per quittare)")
print(" ")
ans=input()
if ans=="yes":
    send_email.mass_email(partecipanti)
else:
    quit()