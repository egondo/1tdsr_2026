#103.910.970-59

cpf = int(input("CPF (9 digitos): "))

aux_work = cpf

soma1 = 0
soma2 = 0 
mult = 2
while aux_work != 0:
    dig = aux_work % 10
    aux_work = aux_work // 10
    #ßßßprint(dig)

    soma1 = soma1 + dig * mult  #somatoria do 1 digito verificador
    mult = mult + 1
    soma2 = soma2 + dig * mult  #somatoria do 2 digito verificador  

resto = soma1 % 11
if resto < 2:
    dc1 = 0
else:
    dc1 = 11 - resto

soma2 = soma2 + dc1 * 2

resto = soma2 % 11
if resto < 2:
    dc2 = 0
else:
    dc2 = 11 - resto


dc = dc1 * 10 + dc2
print(f"Digito de controle do CPF é {dc}")
