print('Hello world!')
print('Hello world!')

# utilizando a mesma funcao, mas com a barra invertida e o n \n:

print('Hello world!\nHello world!')

print('First tentative\nNice! great!')

# Função Concatenar, pode-se juntar duas strings na mesma linha:

print('Guilherme'+'From Promeca') # tudo junto
print('Guilherme ' + 'From Promeca') # com um espaço
print('Guilherme' + ' ' + 'From Promeca') # concatenando diretamente o 'espaço'


reset = '\nReset code'
print(reset)
print('\nDialogo\n')

# a funcao imput gera uma interacao no terminal dando a possibilidade de comunicacao com o codigo
# o imput vem primeiro que a funcao print onde voce escreve uma informação direto pelo console
# ao escrever a informação a função 'input' é substituida pelo que foi escrito

print('Robô:\n Hello,'+ input('Instrução: Inserir seu nome ->'))
print('Robô:\n How are you?\n' + 'Gui:\n' + input('Instrução: Falar como voce está de saúde e em geral outras coisas ->'))
  
login = input('inserir nome de usuário:')
length = len(login)
print(login+" BEM VINDO!")
print(length)

