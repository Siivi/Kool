#Arvu arvamise mäng. 
#Arvuti mõtleb välja arvu nullist sajani. Lase kasutajal pakkuda, 
# mis arvu arvuti välja mõtles. 
# Vale pakkumise korral annab arvuti vihje, 
# kas pakkumine on õigest arvust suurem või väiksem.
#  Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)


from random import randint

any_number = randint(0, 100)
guess = int(input("Paku arv: "))


while guess != any_number:
    if any_number < guess:
        print("Arv on väiksem, kui pakutud arv.")
    else:
        print("Arv on suurem, kui pakutud arv.")
    guess = int(input("Arva uuesti: "))
print("Palju õnne! Arvasid õigesti!")


