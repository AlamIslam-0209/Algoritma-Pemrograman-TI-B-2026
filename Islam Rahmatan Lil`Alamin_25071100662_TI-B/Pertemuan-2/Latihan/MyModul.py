def sapa(nama):
    print(f"halo {nama}")

def kalkulator():
    a = int(input("masukkan niali a: "))
    b = int(input("masukkan niali b: "))
    operator = input("masukkan operator: ")
    match operator:
        case "+" :
            return a + b

        case "-" :
            return a - b
        
        case "*" :
            return a * b

        case "/" :
            return a / b
        
        case _:
            print("operator tidak diketahui")

    


if __name__ == "__main__":
    sapa('akil') 
    sapa("fais")

    print("alam")
    print(kalkulator())
    
