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

def darTroco():
    entrada = float(input("quanto de troco você precisa? "))

    troco = int(entrada*100) #por exemplo, 2.35 -> 235

    #somente moedas de 50, 25 e 1 centavos
    moeda50cent=0
    moeda25cent=0
    moeda1cent=0
    while (troco!=0):
        if(troco>=50):
            troco=troco-50
            moeda50cent=moeda50cent+1
        elif(troco>=25):
            troco = troco-25
            moeda25cent=moeda25cent+1
        elif(troco>=1):
            troco = troco - 1
            moeda1cent = moeda1cent+1
    print("moeda 50 centavos:",moeda50cent)
    print("moeda 25 centavos:",moeda25cent)
    print("moeda 1 centavos:",moeda1cent)

def cabecalho():
    print("=======Mercado do João=======")
    print("Digite os valores dos produtos. Para finalizar, digite 0")

def cobrarCliente(valorTotal): 
    valorPago = get_float("Quanto reais você irá pagar?")
    while(valorTotal>valorPago): 
        valorPago = get_float("Você não deu dinheiro suficiente! Quanto reais você irá pagar?")
    return valorPago


def main(): 
    cabecalho()
    compras = passarCompras()
    valorTotal = sum(compras)
    print(f'O valor total das compras é R$ {valorTotal}')
    valorPago = cobrarCliente(valorTotal)
    print(f'O valor pago será de {valorPago}')

    troco = "{:.2f}".format(valorPago - valorTotal)
    print(f'O troco será de {troco}')

    

if __name__ == '__main__':
    main()