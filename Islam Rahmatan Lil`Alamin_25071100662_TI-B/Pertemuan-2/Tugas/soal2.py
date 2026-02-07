'''
Buat sebuah fungsi bernama bilangan prima(n) yang:
1. Menggunakan range()
2. Mengembalikan list bilangan prima dari 1 sampai n
Kemudian:
1. Panggil fungsi untuk n = 50
2. Tampilkan hasilnya
'''

def bilangan_prima(n):
    prima = [2]
    for i in range(2, n):
        for j in prima:
            if i % j == 0:
                break
        else:
            prima.append(i)
        
    
    return prima

print(bilangan_prima(50))