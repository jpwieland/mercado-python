def get_int():
    while(True):
        try: 
            numero = int(input("Digite um número: "))
            return numero
        except ValueError: 
            print("Você não digitou um número!! :(")

def get_float():
    while(True):
        try: 
            numero = float(input("Digite um número: "))
            return numero
        except ValueError: 
            print("Você não digitou um número!! :(")

def main(): 
    numeroDigitado =  get_int()
    print(numeroDigitado)

if __name__ == '__main__':
    main()