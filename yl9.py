#Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
# Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi.
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

a = float(input("Esimese külje pikkus: "))
b = float(input("Teise külje pikkus: "))
c = float(input("Kolmanda külje pikkus: "))

if  a >= b+c or b >= a+c or c >= a+b:
    print("Sellist kolmnurka ei eksisteeri")
    if a == b == c:
        print("Võrdkülgne")
    elif a == b > c or a == c > b or b == c > a :
        print("Võrdhaarsed")
else:
    print("Erikülgsed")