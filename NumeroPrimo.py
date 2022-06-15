
def numeroPrimo ():

    numero: int = int(input("ingrese numero natural"))

    if numero > 1:
        for i in range(2,int(numero)):
            if (numero) % i == 0:
                print(f"El Numero {numero} No es Primo, es dividido entre {i}")
            break


        else:
            print(f"el número {numero} es primo")

    else:
          print(f"El número {numero} NO ES PRIMO ingrese numero mayor que  1")


print(numeroPrimo())


