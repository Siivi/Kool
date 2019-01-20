#Väljasta korduslause abil 8 korrutis arvudega 0..12 ja vorminda väljund nii:
#8 x 0 = 0
#	8 x 1 = 8
#	8 x 2 = 16
#	…
#	8 x 12 = 96
#Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse

x=int(input("Sisestage arv: "))

multiplier = 1
while multiplier <= 12:
    print(multiplier * x)
    multiplier += 1