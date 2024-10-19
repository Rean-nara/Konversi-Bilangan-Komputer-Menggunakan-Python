#Function Dec Converter
def DecToOct(n):
    if (n > 0):
        return DecToOct(int(n/8)) + str(n%8)
    else:
        return ''
        
Konversi = {0: '0', 1: '1', 2: '2', 3: '3', 
            4: '4', 5: '5', 6: '6', 7: '7', 
            8: '8', 9: '9', 10: 'A', 11: 'B', 
            12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def DecToHex(n):
    if (n > 0):
        sisa = n % 16
        return DecToHex(int(n/16)) + Konversi[sisa]
    else:
        return ''
    
#Function Binary Converter
def BinToDes(n):
    angka = n
    nilaidec = 0
    pangkat = 1
    nilai = angka
    while(nilai):
        nilaiakhir = nilai % 2
        nilai = int(nilai/2)
        nilaidec += nilaiakhir*pangkat
        pangkat = pangkat * 2
    return nilaidec
#Function Octal Converter
def OctToDec(n):
    angka = n
    nilaidec = 0
    pangkat = 1
    nilai = angka
    while (nilai):
        nilaiakhir = nilai % 10
        nilai = int(nilai/10)
        nilaidec += nilaiakhir * pangkat
        pangkat = pangkat * 8
    return nilaidec

def DecToHex(n):
    konversi = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexa = ''
    while n > 0:
        sisa = n % 16
        hexa = konversi[sisa] + hexa
        n = n // 16
    return hexa

#Function Hexa Converter
def HexToDec(n):
    Konversi = {'0': 0, '1': 1, '2': 2, '3': 3,  
         '4': 4, '5': 5, '6': 6, '7': 7, 
         '8': 8, '9': 9, 'A': 10, 'B': 11,  
         'C': 12, 'D': 13, 'E': 14, 'F': 15}
    NilaiDecimal = 0
    Pangkat = len(n)-1
    for digit in n:
        NilaiDecimal += Konversi[digit] * (16 ** Pangkat)
        Pangkat -= 1
    return NilaiDecimal

def DecToOct(NilaiDecimal):
    NilaiOctal = ''
    while NilaiDecimal > 0:
        sisa = NilaiDecimal % 8
        NilaiOctal = str(sisa) + NilaiOctal
        NilaiDecimal = NilaiDecimal // 8
    return NilaiOctal

#Run
print("     Selamat Datang di Konversi Python       ")
print(" Pilih Sistem Bilangan Yang Akan Dikonversi")
print("     1. Desimal   2. Oktal    3. Hexa    4.Biner")
pilihan = int(input())
if pilihan == 1:
    print ("Masukkan Nilai Desimal:")
    Nilai = int(input())
    Oktal = DecToOct(int(Nilai))
    Hex = DecToHex(int(Nilai))
    print ("Hasil Konversi Ke Oktal:", Oktal) 
    print ("Hasil Konversi Ke Hexa:", Hex)
elif pilihan == 2:
    NilaiOctal = input("Masukkan Nilai Oktalnya:")
    NilaiDec = OctToDec(int(NilaiOctal))
    NilaiHex = DecToHex(int(NilaiDec))
    print ("Nilai Octal:", NilaiDec)
    print ("Nilai Hexa:", NilaiHex)
elif pilihan == 3:
    NilaiHexa = input("Masukkan Nilai Hexa:")
    NilaiDecimal = HexToDec(NilaiHexa.upper())
    NilaiOctal = DecToOct(NilaiDecimal)
    print("Nilai Desimal:",NilaiDecimal)
    print("Nilai Octal:",NilaiOctal)
elif pilihan ==4:
    NilaiBiner = input("Masukkan Nilai Biner:")
    NilaiDecimal = BinToDes(NilaiBiner)
    print("Nilai Biner:",NilaiDecimal)
