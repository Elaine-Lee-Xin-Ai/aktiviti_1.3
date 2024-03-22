#Atur cara mengira luas permukaan dan isipadu sebuah tangki air berbentuk silinder
#Isytihar pemalar
pi=3.142

#Input
jejari=float(input("Masukkan jejari:"))
tinggi=float(input("masukkan tinggi:"))

#Proses
luas_permukaan=(2*pi*jejari*jejari)+(2*pi*jejari*tinggi)
isipadu=pi*jejari*jejari*tinggi

#Output
print("Luas permukaan ialah",luas_permukaan)
print("Isipadu ialah",isipadu)
