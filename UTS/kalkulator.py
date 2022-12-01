print('## Progam Membuat Kalkulator ##')
print('================================================')
print('Shofi Syahria Mahram-0110222012-TI09')
print()

#input
print('Kalkulator Dasar Matematika')
print('Jumlah \t [+]')
print('Kurang \t [-]')
print('Bagi \t [/]')
print('Kali \t [*]')
print('Pangkat \t [**]')

print()
x = int(input("masukan angka 1 : "))
y = int(input("masukan angka 2 : "))
operator = input("masukan operator pilihan : ")

#keterangan
if operator == "jumlah":
    hasil = x + y
elif operator == "kurang":
    hasil = x - y
elif operator == "bagi":
    hasil = x / y
elif operator == "kali":
    hasil = x * y
elif operator == "pangkat":
    hasil = x ** y
else :
    print("tidak sesuai")

#ouput
print("Masukan angka 1:", x)
print("Masukan angka 2:", y)
print("Operator yang akan digunakan: ", operator)
print("Hasil kalkulator:", hasil)