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



st1 = 'TANPAMU'
st2 = 'LESU'
st3 = 'KAREPMU'

print('Aku {} ora mungkin {} tapi tetep {}'.format(st1,st2,st3))


for i in range (1,101):
    if i %4:
        print(i)
    else:
        print(i,'Habis di bagi 4')

wow = int(input('masukkan angka : '))
wow2 = int(input('masukan angka : '))

wowpol = wow % wow2 
print(wowpol)


telek = input('masukan 3 kata kak : '(sep='-'))
print('aku', 'suka' , 'kamu',sep='-')


string1 = 'Balonku ada lima'
string2 = 'Rupa rupa warnanya'
string3 = 'Hijau, Kungin, Kelabu'
string4 = 'Merah muda dan biru'
string5 = 'Meletus balon hijau DOR!'
string6 = 'Hatiku sangat kacau'
string7 = 'Balonku tinggal empat'
string8 = 'Kupegang erat-erat'

print(string1.center(50))
print(string2)
print(string3)
print(string4.rjust(50))
print('')
print(string5.rjust(30))
print(string6.rjust(35))
print(string7.rjust(48))
print(string8.rjust(34))
