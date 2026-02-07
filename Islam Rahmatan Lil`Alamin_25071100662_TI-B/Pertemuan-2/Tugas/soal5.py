'''
Buat sebuah program Python yang:
1. Menggunakan module math
2. Membuat fungsi jarak(x1, y1, x2, y2) untuk menghitung jarak dua titik pada
bidang Kartesius
3. Menggunakan rumus resultan
Contoh keluaran:
Jarak = 5.0
'''
import math

def hitungJarakManual(x1, y1, x2, y2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

def jarak(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2, y1)

print(jarak(0, 0, 6, 8))
print(hitungJarakManual(0, 0, 6, 8))
