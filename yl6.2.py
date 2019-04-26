#Kirjuta programm, mis küsib kasutajalt failinime kujul “fail.ext” ja prindib välja faili laienduse. (str.split)


f_name = input("Mis on faili nimi: ")
x = f_name.split(".")[-1]

print("Faili laiendus on ." + str(x))