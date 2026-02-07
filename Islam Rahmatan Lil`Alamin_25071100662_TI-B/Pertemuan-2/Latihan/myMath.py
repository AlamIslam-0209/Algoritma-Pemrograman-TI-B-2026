def tambah(a,b):
    return a + b

def kurang(a,b):
    return a - b 

def kali (a, b):
    return a * b 

def bagi(a, b):
    try:
        return a / b 
    except ZeroDivisionError:
        print("tidak bisa membagi dengan nol")

def modulus(a,b):
    return a % b 

def fibbonaci(n):
    fib = [0, 1]
    for i in range(n-2):
        golden = fib[i] + fib[i+1]
        fib.append(golden)
    return fib
    
    


