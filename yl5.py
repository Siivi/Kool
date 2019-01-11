# Kirjuta programm, mis teisendab kasutaja poolt kroonides
# sisestatud summa eurodesse ja väljastab tulemuse.

sum_k=int(input("Sisestage summa kroonides: "))

eur= (float(sum_k/15.6466))
x= round(eur, 2)

print(x)