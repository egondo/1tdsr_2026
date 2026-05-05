def is_bissexto(ano: int) -> bool:
    '''quando o ano é bissexto:
    a) multiplo de 4
    b) anos múltiplos de 100 não são bissextos, exceto 
    quando são múltiplos de 400'''
    if ano % 400 == 0:
        return True
    if ano % 100 == 0:
        return False
    if ano % 4 == 0:
        return True
    return False
    

def valida_data(dia: int, mes: int, ano: int) -> bool:
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    if dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        return False

    if mes == 2:
        if dia > 29:
            return False
        if dia == 29 and not is_bissexto(ano):
            return False

    if ano <= 0:
        return False
    
    return True


print('31/2/1978', valida_data(31, 2, 1978))
print('29/2/1976', valida_data(29, 2, 1976))
print('31/11/1980', valida_data(31, 11, 1980))
