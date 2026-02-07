'''
Buat sebuah fungsi bernama rata rata(nilai) yang:
1. Menerima sebuah list berisi nilai mahasiswa
2. Menghitung rata-rata nilai
3. Jika list kosong, kembalikan pesan: "Data kosong"
Kemudian:
1. Panggil fungsi dengan list: [80, 75, 90, 60, 85]
2. Tampilkan hasilnya
'''

def rata_rata(nilai):
    return sum(nilai) / len(nilai) if len(nilai) > 0 else 0

nilai = [80, 75, 90, 60, 85]
nilai1 = []

print(f"{rata_rata(nilai)}")
print(f"{rata_rata(nilai1)}")
