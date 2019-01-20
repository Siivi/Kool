#Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
#Väljasta listi esimene väärtus
#Lisa listi lõppu uus puuvili
#Väljasta listi viimane väärtus
#Muuda ühe elemendi väärtust ja väljasta kogu list
#Kontrolli kas väärtus (näiteks õun) eksisteerib listis
#Väljasta listi pikkus
#Eemalda listist element ja väljasta kogu list
#Muuda listi järjekord vastupidiseks
#Sorteeri list ja väljasta
#(jada, list, listi element, listi funktsioonid)
#https://www.w3schools.com/python/python_lists.asp



my_list = ["kiwi","plum","apple"]
print (my_list[0])
my_list.append ("pear")
print (my_list[3])
my_list[2] = "orange"
print (my_list)
if "apple" in my_list:
    print ("Yes, 'apple' is in the list")
else:
    print ("No, there is no 'apple' in the list ")
print (len(my_list))
my_list.remove ("plum")
print (my_list)
my_list.reverse ()
print (my_list)
my_list.sort ()
print (my_list)