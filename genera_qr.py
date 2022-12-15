import csv
import qrcode

def make_qr(partecipante):
  img=qrcode.make("https://cc2022.esnpolimi.it/ticket.php?id="+partecipante.hash)
  img.save('output/qrcode.png')

