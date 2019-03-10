#Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud
#  täisarv on paarisarv või mitte. (paarisarvu mõiste - odd/even)

num = int(input("Sisestage number: "))

if (num % 2) == 0:
    print ("{0} on paarisarv".format(num))
else:
    print("{0} ei ole paarisarv".format(num))

# Python program to check if the input number is odd or even.
# A number is even if division by 2 give a remainder of 0.
# If remainder is 1, it is odd number.