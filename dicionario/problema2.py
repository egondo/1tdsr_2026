def inverte_dicionario(d: dict) -> dict:
    retorno = {}
    for termo_ingles in d:
        termo_pt = d[termo_ingles]
        if not termo_pt in retorno:
            retorno[termo_pt] = termo_ingles
        else:
            print(f"{termo_pt} aparece mais de uma vez")
    return retorno

en_pt = {"house": "casa", "dog": "cão", 
         "cat": "gato", "mouse": "rato"}

pt_en = inverte_dicionario(en_pt)

for chave in pt_en:
    print(chave, "->", pt_en[chave])