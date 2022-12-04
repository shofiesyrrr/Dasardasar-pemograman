#input
Nama = input("masukan nama anda : ")
Umur = input("masukan umur anda : ")
Tinggi = input("masukan tinggi anda : ")

#logika
if int(Tinggi) >= 90 :
    ket = "Anda boleh bermain"
else :
    ket = "Anda tidak boleh bermain"

#output
print("Nama anda :", Nama)
print("Umur anda :", Umur)
print("Tinggi anda :", Tinggi)
print(ket)