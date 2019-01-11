#Kirjutada programm, mis kontrollib, kas antud positiivne
#  täisarv on liig- või lihtaasta number. 
# (Aasta on liigaasta, kui tema number jagub neljaga, 
# välja arvatud need aastad, mille number jagub sajaga, kuid ei jagu neljasajaga.)

num= int(input("Sisestage number: "))


if num % 4 == 0  and num % 100 != 0 or num % 400 == 0: 
    print("Aasta on liigaasta.")
else:
    print("Aasta ei ole liigaasta.")
