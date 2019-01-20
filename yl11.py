#Kasutaja sisestab oma lemmiklooma, väljasta väljasta selle muutuja esimene täht
#Koosta list, mis koosneb kolmest loomast, lisa selle listi lõppu kasutaja lemmikloom, väljasta list,
# väljasta listi viimase elemendi viimane täht
#(sõne kui list, mitmemõõtmeline list - multi dimensional)

pet = input ("Who is your pet? ")
your_list = list (pet)
print (your_list[0])
my_list = ["cat", "bunny", "gold fish", pet]
print (my_list)
c_list = list (my_list)
print (c_list[-1][-1])

