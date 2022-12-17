import csv
import bcrypt
import pickle
import os
from datetime import datetime


class persona:
    def __init__(self,nome,cognome,email):
        self.nome=nome
        self.cognome=cognome
        self.email=email
        self.hash=get_hashed_password(self.nome+self.cognome)[7:17]
        

def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt(5))


def save_partecipanti_list(partecipanti,input_file):
    now = datetime.now()
    dt_string = now.strftime("_%d-%H:%M:%S")
    tempTuple = os.path.splitext(input_file)
    input_file = "output/"+tempTuple[0]+"_lista"+dt_string
    with open(input_file, 'wb') as fp:
#    with open("output/dump_lista", 'wb') as fp:
        pickle.dump(partecipanti, fp)
        print('Done writing list into a binary file')

def save_partecipanti_totali(partecipanti,nome_file):
    with open("output/"+nome_file, 'wb') as fp:
#    with open("output/dump_lista", 'wb') as fp:
        pickle.dump(partecipanti, fp)
        print('Done writing list into a binary file')


def load_partecipanti_list(input_file):
    with open("output/"+input_file, 'rb') as fp:
        partecipanti=pickle.load(fp)
    return partecipanti

def get_partecipanti(filename):
    partecipanti=[]
    with open("input/"+filename, 'r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            partecipanti.append(persona(lines["Nome"],lines["Cognome"],lines["Email"]))
    file.close()
    save_partecipanti_list(partecipanti, filename)
    return partecipanti

def generate_SQL_dump(partecipanti):
    now = datetime.now()
    dt_string = now.strftime("_%d-%H:%M:%S")
    with open("output/SQL_dump_"+dt_string+".txt", 'a') as f:
        f.write("INSERT INTO `utenti`(`Id`, `Nome`, `Cognome`, `Usato`) VALUES ")
        for partecipante in partecipanti:
            f.write("('"+partecipante.hash+"', '"+partecipante.nome+"', '"+partecipante.cognome+"', 0), ")
    f.close()         

def print_partecipanti(partecipanti):
    for partecipante in partecipanti:
        print(partecipante.hash+" "+partecipante.nome+" "+partecipante.cognome+" "+partecipante.email)

def find_partecipante_cognome(partecipanti,cognome):
    for partecipante in partecipanti:
        if partecipante.cognome.lower()==cognome.lower():
            return partecipante
    print(f"{cognome} non trovato")
    return()

#partecipanti=get_partecipanti("partecipanti_prova.csv")
#partecipanti=load_partecipanti_list("partecipanti_prova_lista")
