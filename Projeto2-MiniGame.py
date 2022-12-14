# ### Desafio 1 

# Monte um mini-game turtle, que possibilite que o usuário controle para qual direção a tartaruga deve andar(frente/trás) e qual ângulo deverá ser tomado a cada nova movimentação

# ### Desafio 2 

# Usando o mini-game, desenha um quadrado passando instruções para a turtle, totalmente através do input do usuário

# #### Dicas Iniciais

# * Crie uma nova turtle primeiro

# * Coloca seu programa em loop 

# * Faça perguntas ao usuário para decidir se a tartaruga deve movimentar para frente ou para trás

# * Após decidir se ele deve movimentar para frente ou para trás, receba do usuário quantos pixels devem ser percorridos

# * Faça perguntas ao usuário para decidir se a tartaruga deve rotacionar para esquerda ou direta

# * Após decidir se ele deve rotacionar para esquerda ou direita, receba do usuário quantos pixels devem ser rotacionados

# * Ao executar essa ação pergunte ao usuário "Continuar andando?", e reaga de acordo com a resposta do usuário.

# #### Dicas Adicionais

# * Não esqueça de converter o input do usuário para o tipo apropriado

# * Resolva um problema de cada vez e lembre de seguir a seguinte lógica: 

# Pergunte -> Processe resposta -> A

from turtle import Turtle
t=Turtle()
t.speed(1)
while True:
   direção= input('Para qual direção desseja ir? f:frente t: tras ')
   if direção =='f':
     distancia= int(input('Qual a distancia a percorrer? '))
     t.forward(distancia)
   elif direção =='t':
     distancia= int(input('Qual a distancia a percorrer? '))
     t.backward(distancia)
   else:
    print('Opção Inválida')

   rotação= input('Deseja virar o cursor? d: direita e: esquerda n:nao ')
   if rotação=='d':
    angulo= int(input('Quantos graus deseja virar? '))
    t.right(angulo)
   elif rotação == 'e':
    angulo= int(input('Quantos graus deseja virar? '))
    t.left(angulo)
   elif rotação== 'n':
    parar = input('Continuar andando? s/n ')
    if parar =='n':
        break
     
    
