#input
nama_kendaraan=input("masukan nama kendaraan : ")
jenis_bensin=input("masukan jenis bensin : ")
kota_yang_dituju=input("kota yang di tuju : ")

#rumus
if jenis_bensin=="pertalite":
    harga=10000
    jarak_tempuh=12
elif jenis_bensin=="pertamax":
    harga=14000
    jarak_tempuh=13
elif jenis_bensin=="pertamax turbo":
    harga=17000
    jarak_tempuh=13.5
else:
    print("habis")

if kota_yang_dituju=="jakarta":
    jarak_kota=20
elif kota_yang_dituju=="bekasi":
    jarak_kota=35.7
elif kota_yang_dituju=="depok":
    jarak_kota=5
elif kota_yang_dituju=="tanggerang":
    jarak_kota=99
elif kota_yang_dituju=="bogor":
    jarak_kota=120.6
else:
    print("kota tidak di ketahui")
    
pemakaian_bensin=jarak_kota/jarak_tempuh
total_harga_bensin=pemakaian_bensin*harga

print("pemakaian bensin : ", pemakaian_bensin)
print("total harga bensin : ", total_harga_bensin)