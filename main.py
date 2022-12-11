import genera_utenti
import genera_qr
import send_email

partecipanti=genera_utenti.get_partecipanti("input/partecipanti_prova.csv")
genera_utenti.generate_SQL_dump(partecipanti)
send_email.mass_email(partecipanti)