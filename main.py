import genera_utenti
import genera_qr
import send_email
import sys

menu_options = {
    1: 'Option 1',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option0():
    partecipanti_nuovi=genera_utenti.get_partecipanti(sys.argv[1])
    genera_utenti.print_partecipanti(partecipanti_nuovi)
    genera_utenti.generate_SQL_dump(partecipanti_nuovi)
    print("Partecipanti caricati su DB? (yes per continuare, invio per quittare)")
    print(" ")
    ans=input()
    if ans=="yes":
        send_email.mass_email(partecipanti_nuovi)
        partecipanti=(genera_utenti.load_partecipanti_list("lista_partecipanti"))
        partecipanti.extend(partecipanti_nuovi)
        genera_utenti.save_partecipanti_totali(partecipanti, "lista_partecipanti")
    else:
        quit()
    quit()

def option1():
    partecipanti=genera_utenti.load_partecipanti_list("form_finale_giusto_lista_15-18:48:19")
    genera_utenti.print_partecipanti(partecipanti)
    print("yes per continuare, invio per quittare")
    print(" ")
    ans=input()
    if ans=="yes":
        send_email.mass_email(partecipanti)
    else:
        quit()
    quit()

def option2():
    partecipanti=genera_utenti.load_partecipanti_list("form_finale_giusto_lista_15-18:48:19")
    genera_utenti.print_partecipanti(partecipanti)
    
    print("yes per continuare, invio per quittare")
    print(" ")
    ans=input()
    if ans=="yes":
        send_email.mass_email(partecipanti)
    else:
        quit()
    quit()

def option3():
    partecipanti=(genera_utenti.load_partecipanti_list("lista_partecipanti"))
    
    
    print(genera_utenti.find_partecipante_cognome(partecipanti, "sibony"))
    genera_utenti.save_partecipanti_totali(partecipanti, "lista_partecipanti")

if __name__=='__main__':
    if len(sys.argv)==2:
        option0()
    elif len(sys.argv)>2:
        print("troppi argomenti, scrivi solo il nome del cvs o niente per accedere al menu")
        quit()

    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')


# if len(sys.argv)<2:
#     partecipanti=genera_utenti.load_partecipanti_list("form_finale_giusto_lista_15-18:48:19")
#     genera_utenti.print_partecipanti(partecipanti)
#     print("yes per continuare, invio per quittare")
#     print(" ")
#     ans=input()
#     if ans=="yes":
#         send_email.mass_email(partecipanti)
#     else:
#         quit()
#     quit()
#     #send_email.mass_email(partecipanti)
# if len(sys.argv)>2:
#     print("too many arguments, input only the file name")
#     quit()
# else:
#     partecipanti=genera_utenti.get_partecipanti(sys.argv[1])
#     genera_utenti.print_partecipanti(partecipanti)
# genera_utenti.generate_SQL_dump(partecipanti)
# print("Partecipanti caricati su DB? (yes per continuare, invio per quittare)")
# print(" ")
# ans=input()
# if ans=="yes":
#     send_email.mass_email(partecipanti)
# else:
#     quit()