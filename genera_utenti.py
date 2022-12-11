import csv
import bcrypt
class persona:
    def __init__(self,nome,cognome,email):
        self.nome=nome
        self.cognome=cognome
        self.email=email
        self.hash=get_hashed_password(self.nome+self.cognome)[7:17]
    
def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt(5))

def get_partecipanti(filename):
    partecipanti=[]
    with open(filename, 'r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            partecipanti.append(persona(lines["Nome"],lines["Cognome"],lines["Email"]))
    file.close()
    return partecipanti

def generate_SQL_dump(partecipanti):
    with open('output/SQL_dump.txt', 'a') as f:
        f.write("INSERT INTO `utenti`(`Id`, `Nome`, `Cognome`, `Usato`) VALUES ")
        for partecipante in partecipanti:
            f.write("('"+partecipante.hash+"', '"+partecipante.nome+"', '"+partecipante.cognome+"', 0), ")
            #modifcare per generare un unica query
    f.close()         



# partecipanti=get_partecipanti("input/partecipanti.csv")
# generate_SQL_dump(partecipanti)

# for partecipante in partecipanti:
#     print(partecipante.nome+ " "+partecipante.cognome+" "+partecipante.email+" "+ partecipante.hash)


