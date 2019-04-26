#Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9. Arvuta n + nn + nnn väärtus ja väljasta see. 
# (Näiteks kui kasutaja sisestab 2, siis on vaja väljastada tulemus 2 + 22 + 222 = 246)

n = int(input("Sisesta täisarv vahemikus 1-9: "))

nn = int(str(n)+str(n))

nnn = int(str(nn)+str(n))

num = n + nn + nnn

print("Tehte n + nn + nnn väärtus on " + str(num))

