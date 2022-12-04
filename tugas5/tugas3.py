print("Menghitung berat badan ideal")
print("")

#input
tinggibadan = input("masukan tinggi badan anda ( cm )= ")

#rumus
tinggibadan2= (int(tinggibadan)-100)*10/100
beratideal= (int(tinggibadan)-100)-int(tinggibadan2)

#output
print("berat badan ideal anda adalah?", beratideal, "kg")
