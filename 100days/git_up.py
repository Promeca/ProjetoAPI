print("     BEM VINDO, AO PROMECO BISTRÔ!        \n")

# Primeiro, pedimos ao usuário para inserir o total do serviço, o número de pessoas e a porcentagem da gorjeta.
total_service = float(input(':) Insira o total do serviço consumido: R$'))
total_people =  int(input(':) Quantas pessoas para contribuir com o serviço oferecido?'))

# Usamos um loop while para garantir que a porcentagem inserida seja uma das opções sugeridas.
percent = float(input(':) Insira a porcentagem desejada pelo serviço: 10, 12, 15'))
while percent not in [10, 12, 15]:
    print("Por favor, insira uma das porcentagens sugeridas: 10, 12 ou 15.")
    percent = float(input(':) Insira a porcentagem desejada pelo serviço: 10, 12, 15'))

# Agora que temos todas as informações necessárias, podemos calcular a gorjeta.
gorjeta = (percent/ 100) * total_service 

# Em seguida, dividimos a gorjeta pelo número de pessoas para obter a gorjeta por pessoa.
gorjeta_por_pessoa = gorjeta/ total_people

# Definimos a mensagem base.
mensagem = str(gorjeta_por_pessoa) + ' reais o total de gorjeta por pessoa'

# Se o número total de pessoas for maior que 1, adicionamos a parte "ao dividir por..." à mensagem.
if total_people > 1:
    mensagem += ', ao dividir por ' + str(total_people)

# Adicionamos a parte final da mensagem.
mensagem += ', obrigado :)'

# Imprimimos a mensagem.
print(mensagem)