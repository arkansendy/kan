for i in range (1,56):
    if i %5 :
        print(i)
    else:
        print(i, "kelipatan 5")

i = 2
while (i < 30):
    j = 2
    while(j <= (i/j)):
        if not(i%j):break
        j=j+1
    if(j > i/j): print(i, ' bilangan prima ')
    i=i+1



bebek = int(input("Masukkan jumlah anak bebek: "))

#setoutput
if bebek >= 2:
    while bebek > 1:
        print("Anak bebek turun %e mati 1 tinggal %e"%(bebek,bebek-1))
        bebek = bebek - 1
if bebek <= 1:
    print("Anak bebek turun %e mati 1 tinggal induknya"%(bebek))
else:
    print("Anak bebek ada %e tumbas meneh ben akeh"%(bebek))

angka = -1
if angka >= 0:
    print("Angka Positif atau Nol")
else:
    print("Angka Negatif")

print('jempol' , ' sikil ' , 'otal atil' , sep="-")