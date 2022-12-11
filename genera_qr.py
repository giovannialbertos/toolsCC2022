import csv
import qrcode

def make_qr(partecipante):
  img=qrcode.make("http://cc2022.esnpolimi.it/ticket.php?id="+partecipante.hash)
  img.save('output/qrcode.png')




# file = open("idsCC2022.csv", "r")
# data = list(csv.reader(file, delimiter=","))
# file.close()
# ids = []
# for nums in data:
#   for val in nums:
#     ids.append(val)
# print(ids)

# #data = 'http://localhost/CC2022/public/ticket.php?id='+ids[0]
# #per sito vero :
# data = 'http://cc2022.esnpolimi.it/ticket.php?id=ciao'

# # Encoding data using make() function
# img = qrcode.make(data)

# # Saving as an image file
# img.save('MyQRCode2.png')