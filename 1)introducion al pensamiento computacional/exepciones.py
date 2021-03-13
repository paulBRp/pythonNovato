def divide_elementos_de_la_lista(lista, divisor):
    try:
        return[i/divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista =list(range(10))
divisor=1
print(f'elementos: {divide_elementos_de_la_lista(lista,divisor)}')