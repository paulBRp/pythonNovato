def busca_pais(country, pais):
    """ 
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.
    """

    try:
        return paises[pais]
    
    except KeyError:
        returnNone

paises = {'ec':'ecuador','col':'colombia','pe':'peru'}
pais = 'pe'
print(busca_pais(paises,pais))