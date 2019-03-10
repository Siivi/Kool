#Kirjuta programm, mis leiab kolmest kasutaja poolt 
# sisestatud arvust maksimumi (ära kasuta max funktsiooni)

num1= int(input("Sisestage esimene arv: "))
num2= int(input("Sisestage teine arv: "))
num3= int(input("Sisestage kolmas arv: "))

if num1>num2 and num1>num3:
    print(str(num1) + " on teistest suurem!")
elif num2>num1 and num2>num3:
    print(str(num2) + " on teistest suurem!" )
else:
    print(str(num3) + " on teistest suurem!")
