def get_int(texto = "Digite um número"):
    while(True):
        try: 
            numero = int(input(texto))
            return numero
        except ValueError: 
            print("Você não digitou um número!! :(")

def get_float(texto = "Digite um número"):
    while(True):
        try: 
            numero = float(input(texto))
            return numero
        except ValueError: 
            print("Você não digitou um número!! :(")

def passarCompras():
    valorProdutos = [] 
    numeroDigitado = get_float("Digite o valor do produto ")
    while(numeroDigitado != 0):
        valorProdutos.append(numeroDigitado)
        numeroDigitado = get_float("Digite o valor do próximo produto ")
    return valorProdutos

        
def main(): 
    print("=======Mercado do João=======")
    print("Digite os valores dos produtos. Para finalizar, digite 0")
    compras = passarCompras()
    print(compras)
    print(f'O valor total das compras é R$ {sum(compras)}')
    

if __name__ == '__main__':
    main()