#Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, 
# küsib kasutajalt elukoha, kui elukoht on Saaremaa, siis väljastab mingi kommentaari,
#  küsib kasutajalt vanuse, kui vanus on väiksem kui 18, siis ütleb, 
# et kasutaja on liiga noor, et autot juhtida, kui vanus on 18,
#  siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18,
#  siis ütleb, et kasutaja võib autot juhtida. (sõne - string)


name= input("Sisestage nimi: ").capitalize()

print("Tere " + str(name) + "!")

place= input("Kus te elate: ").capitalize()


if place== "Saaremaa" or "Saaremaal":
    print("On kaunis koht, see "+ place +"!")

age= int(input("Kui vana te olete: "))
if age < 18:
    print(name + " olete liiga noor, alles " + str(age) + " aastat vana, et autot juhtida!")
elif age == 18:
    print(name + "! Palju õnne, täisealiseks saamise puhul!!!")
else:
    print(name + " võite autot juhtida.")