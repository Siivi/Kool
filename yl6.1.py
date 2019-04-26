#Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)


import math
rad = int(input("Sisestage raadius:"))


#ringi ümbermõõt = pii korda 2 korda raadius
#ringi pindala = pii korda raadius ruudus

circ = round(math.pi*2*rad)
area = round(math.pi*rad**2)

print("Ringi pindala on " + str(area))
print("Ringi ümbermõõt on "+ str(circ))

