'''
Buat sebuah fungsi rekursif bernama pangkat rekursif(a, b) yang:
1. Menghitung nilai a pangkat b
2. Tidak boleh menggunakan operator pangkat (**)
3. Harus menggunakan rekursi
Contoh:
Input: a = 2, b = 5
Output: 32
'''

def pangkat_rekursif(a, b):
    b -= 1
    if b == 0:
        return a
    return pangkat_rekursif(a, b) * a

print(pangkat_rekursif(2, 5))
