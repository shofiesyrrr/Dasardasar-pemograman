#input
nama = input("masukan nama anda : ")
nilai = input ("masukan nilai anda :")
kelas = input("masukan kelas anda : ")

#rumus
if int(nilai) > 89 :
    ket = "istimewa"
elif int(nilai) > 69 :
    ket = "sangat bagus"
elif int(nilai) > 59 :
    ket = "cukup"
else :
    ket = "gagal"

#output
print("nama anda :", nama)
print("nilai anda :", nilai)
print("kelas anda :", kelas)
print(ket)