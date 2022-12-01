print('##  Program Python Menghitung Luas Trapesium  ##')
print('================================================')
print('Shofi Syahria Mahram-0110222012-TI09')
print()
  
sisi_atas = float(input('Input panjang sisi sejajar atas: '))
sisi_bawah = float(input('Input panjang sisi sejajar bawah: '))
tinggi = float(input('Input tinggi trapesium: '))
 
luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi ;
 
print('Luas trapesium adalah =',round(luas,2))