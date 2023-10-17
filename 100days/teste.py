# Criae um programa que verifique quando dado um ano qualquer se esse ano é bissexto:

# Um ano normal tem 365 dias, anos bissextos têm 366, com um dia a mais em fevereiro.

# A regra para um ano ser bissexto é que ele deve ser 
# divisível por 4, mas não por 100, a menos que também seja divisível por 400.

year = int(input("Insira o ano:"))
print(f"Ano: {year} ")

etapa_1 = year % 4      # o modulo % ele traz o resto da divisao
etapa_2 = year % 100    # o modulo % ele traz o resto da divisao
etapa_3 = year % 400    # o modulo % ele traz o resto da divisao

if etapa_1 == 0: # se na etapa 1 o resto for 0, significa que nao sobrou restos, entao passou para a proxima etapa:
    if etapa_2 == 0: # se nao for por 100 é bissexto se for passa pra proxima:
        if etapa_3 == 0:
            print("É um ano bissexto!")
        else:
            print("Não é bissexto!")
    else:
        print("É um ano bissexto!")
else:
    print("Não é bissexto!")