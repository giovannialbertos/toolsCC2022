import genera_utenti
import genera_qr
import send_email

partecipanti=genera_utenti.get_partecipanti("input/partecipanti_prova.csv")
print(partecipanti[0].hash)
send_email.mass_email(partecipanti)