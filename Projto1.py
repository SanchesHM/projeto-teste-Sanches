# PROJETO 1 

## Objetivo de projeto

# * Estamos criando um módulo de login do nosso aplicativo, e você deve obter as seguintes informações do funcionário.

## Módulo 1 - Gerar registro do funcionário

### Funcionalidades do módulo 1
'''

1. Obtenha o nome do usuário

2. Obtenha a idade do usuário

3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro

4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
'''

cartoes = ['R$50,00','R$250,00','R$120,00']

'''
5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
'''

## Módulo 2 - Gerar apresentação do usuário

### Funcionalidades do módulo 2 - Mensagem de boas vindas!
'''
Usando os dados obtidos no módulo 1, exiba as seguintes informações:

1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).

Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).
'''

'''
5Q's  1- Dados de entrada: nome, idade, data de registro, data de aniversário
2- Devo criar um cadastro para funcionários e gerar de forma automática um cartão de compras com valor aleatório. Após exibir uma mensagem com 
essas informações para o usuário.
3- O valor do cartão deve ser gerado de forma aleatória e automática.
    Necessário fazer um registro antes de gerar o cartão. contendo o nome, idade e data de registro.
4- O resultado esperado é: Deve ser exibida a mensagem confirmando o cadastro e o valor do cartão concedido.

5- 1- Iniciar o programa de cadastro
    2- input (solicitar) o nome do usuário
    3- input (solicitar) a idade do usuário
    4- input automático data do registro
    5- sortear um valor de cartão
    6- input (solicitar) data do proximo aniversário
    7- print (exibir) a mensagem lá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).
        Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado) '''
import random
from datetime import datetime
nome =input('Olá! Seja bem vindo ao seu cadastro! \nPara iniciarmos, por favor Informe seu nome completo: ')
idade= int(input('Informe sua idade: '))

data_registro= datetime.today()



cartoes = ['R$50,00','R$250,00','R$120,00']
liberado = random.choice(cartoes)


Aniversário= datetime.strptime(input('Informe sua data de nascimento: '),"%d/%m/%Y")

print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {data_registro}. \nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {liberado}.')
