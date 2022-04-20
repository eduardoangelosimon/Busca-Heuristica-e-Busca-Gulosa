import numpy as np

class Cidade: 
  
  def __init__(self, nome_cidade, distancia_objetivo):
    self.nome_cidade = nome_cidade #Nome da cidade
    self.visitado = False #Se a cidade foi visitada
    self.distancia_objetivo = distancia_objetivo # a distancia da cidade do objetivo
    self.vizinhas = [] #cidades vizinhass a cidade fixa
  
  def adiciona_adjacente(self, adjacente):
    self.vizinhas.append(adjacente)

  def mostrar_adjacente(self):
    for interator in self.vizinhas:
      print(interator.cidade.nome_cidade)
  
class Adjacente:
    def __init__(self, cidade, custo):
      self.cidade = cidade
      self.custo = custo
      self.distancia_aestrela = cidade.distancia_objetivo + self.custo

# Nosso Grafo
class Mapa:
    vilaVelha = Cidade('Vila Velha', 0)
    vitoria = Cidade('Vitória', 4)
    serra = Cidade('Serra', 24)
    cariacica = Cidade('Cariacica', 16)
    viana = Cidade('Viana', 18)
    guarapari = Cidade('Guarapari', 41)
    fundao = Cidade('Fundão', 47)
    domingosMartins = Cidade('Domingos Martins', 39)
    marechalFloriano = Cidade('Marechal Floriano', 41)
    pedraAzul = Cidade('Pedra Azul', 76)
    vendaNovaDoImigrante = Cidade('Venda Nova do Imigrante', 88)
    castelo = Cidade('Castelo', 97)
    santaLeopoldina = Cidade('Santa Leopoldina', 37)
    anchieta = Cidade('Anchieta', 65)
    cachoeiroDoItapemirim = Cidade('Cachoeiro do Itapemirim', 103)
    aracruz = Cidade('Aracruz', 49)
    santaTeresa = Cidade('Santa Teresa', 56)
    joaoNeiva = Cidade('João Neiva', 58)

    vilaVelha.adiciona_adjacente(Adjacente(guarapari, 41)),
    vilaVelha.adiciona_adjacente(Adjacente(vitoria, 4)),           
    vilaVelha.adiciona_adjacente(Adjacente(cariacica, 16)),
    
    vitoria.adiciona_adjacente(Adjacente(vilaVelha, 4)),
    vitoria.adiciona_adjacente(Adjacente(cariacica, 14)),
    vitoria.adiciona_adjacente(Adjacente(serra, 21)),
    
    serra.adiciona_adjacente(Adjacente(vitoria, 21)),
    serra.adiciona_adjacente(Adjacente(cariacica, 20)),
    serra.adiciona_adjacente(Adjacente(fundao, 24)),
    
    cariacica.adiciona_adjacente(Adjacente(viana, 16)),
    cariacica.adiciona_adjacente(Adjacente(vitoria, 14)),
    cariacica.adiciona_adjacente(Adjacente(serra, 20)),
    cariacica.adiciona_adjacente(Adjacente(vilaVelha, 16)),
    
    viana.adiciona_adjacente(Adjacente(cariacica, 16)),
    viana.adiciona_adjacente(Adjacente(guarapari, 30)),
    viana.adiciona_adjacente(Adjacente(domingosMartins, 18)),
    
    guarapari.adiciona_adjacente(Adjacente(viana, 30)),
    guarapari.adiciona_adjacente(Adjacente(vilaVelha, 41)),
    guarapari.adiciona_adjacente(Adjacente(anchieta, 19)),
    guarapari.adiciona_adjacente(Adjacente(cachoeiroDoItapemirim, 74)),
    
    fundao.adiciona_adjacente(Adjacente(serra, 24)),
    fundao.adiciona_adjacente(Adjacente(aracruz, 29)),
    fundao.adiciona_adjacente(Adjacente(santaTeresa, 20)),
    fundao.adiciona_adjacente(Adjacente(joaoNeiva, 20)),
    
    domingosMartins.adiciona_adjacente(Adjacente(viana, 18)),
    domingosMartins.adiciona_adjacente(Adjacente(marechalFloriano, 7))

mapa = Mapa()

class VetorOrdenado: # Armazena as cidades vizinhass

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    # Mudança no tipo de dados
    self.valores = np.empty(self.capacidade, dtype=object)

  # Referência para a cidade e comparação com a distância para o objetivo

  def insere(self, adjacente):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return
    posicao = 0
    for interator in range(self.ultima_posicao + 1): # Percorre todo o vetor
      posicao = interator
      if self.valores[interator].distancia_aestrela > adjacente.distancia_aestrela:
        break
      if interator == self.ultima_posicao: # Caso para atualiza última posição
        posicao = interator + 1
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x] # desloca valores para inserção
      x -= 1
    self.valores[posicao] = adjacente
    self.ultima_posicao += 1

  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for interator in range(self.ultima_posicao + 1):
        print(interator, ' - ', self.valores[interator].cidade.nome_cidade, ': ',
              self.valores[interator].custo, ' - ',
              self.valores[interator].cidade.distancia_objetivo, ' - ',
              self.valores[interator].distancia_aestrela)
        
class AEstrela:
  def __init__(self, objetivo):
    self.objetivo = objetivo # --- self.parametro --> atributo
    self.encontrado = False

  def buscar(self, atual): # Função de teste de objetivo
    print('---------')
    print('Atual: {}'.format(atual.nome_cidade))
    atual.visitado = True # Marca o atual como visitado

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenado(len(atual.vizinhas)) # Criar um vetor ordenado com tamanho da quantidade
      for adjacente in atual.vizinhas: # Percorre a lista de vizinho do Grafo atual
        if adjacente.cidade.visitado == False: # Se o vizinho ainda não foi visitado
          adjacente.cidade.visitado = True # Marcar como visitado
          vetor_ordenado.insere(adjacente) # Inserir dentro do vetor ordenado como um vizinho do nó atual
      vetor_ordenado.imprime() # Mostra os vizinhos do nó atual

      if vetor_ordenado.valores[0] != None: # Se o vetor ordenado tiver algum objeto no início
        self.buscar(vetor_ordenado.valores[0].cidade) # Busca pelo início do vetor ordenado

class BuscaGulosa:
  def __init__(self, objetivo):
    self.objetivo = objetivo # --- self.parametro --> atributo
    self.encontrado = False

  def buscar(self, atual): # Função de teste de objetivo
    print('---------')
    print('Atual: {}'.format(atual.nome_cidade))
    atual.visitado = True # Marca o atual como visitado

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenado(len(atual.vizinhas)) # Criar um vetor ordenado com tamanho da quantidade
      for adjacente in atual.vizinhas: # Percorre a lista de vizinho do Grafo atual
        if adjacente.cidade.visitado == False: # Se o vizinho ainda não foi visitado
          adjacente.cidade.visitado = True # Marcar como visitado
          vetor_ordenado.insere(adjacente) # Inserir dentro do vetor ordenado como um vizinho do nó atual
      vetor_ordenado.imprime() # Mostra os vizinhos do nó atual

      if vetor_ordenado.valores[0] != None: # Se o vetor ordenado tiver algum objeto no início
        self.buscar(vetor_ordenado.valores[0].cidade) # Busca pelo início do vetor ordenado

      if vetor_ordenado.valores[0] == None:
        self.buscar # Voltar para a cidade pai anterior e percorrer os outros adjacentes

while True:
  mapa = Mapa()

  while True:
    try:
      print("1 - Busca Gulosa")
      print("2 - Busca AEstrela")
      print("0 - Sair")
      print(" ")

      opcao = int(input("Escolha uma opção: "))
      break
    except:
      print("Digite uma opção válida!")

  if opcao == 0:
    print("Você saiu do programa!")
    break

  elif (opcao != 1 and opcao != 2):
    print("Você escolheu uma opção inválida! Escolha outra opção.")

  elif (opcao == 1):
    print(" ")
    print("Você escolheu a Busca Gulosa.")
    print(" ")
    print("O destino padrão é Vila Velha.")
    print(" ")
    print("1 - Vitória")
    print("2 - Serra")
    print("3 - Cariacica")
    print("4 - Viana")
    print("5 - Guarapari")
    print("6 - Fundão")
    print("7 - Domingos Martins")
    print("8 - Marechal Floriano")
    print("9 - Pedra Azul")
    print("10 - Venda Nova do Imigrante")
    print("11 - Castelo")
    print("12 - Santa Leopoldina")
    print("13 - Anchieta")
    print("14 - Cachoeiro do Itapemirim")
    print("15 - Aracruz")
    print("16 - Santa Teresa")
    print("17 - João Neiva")
    print(" ")
    cidade_partida = int(input("Escolha é a cidade de partida: "))

    if cidade_partida == 1: 
      cidade_partida = mapa.vitoria

    elif cidade_partida == 2: 
      cidade_partida = mapa.serra
    
    elif cidade_partida == 3: 
      cidade_partida = mapa.cariacica

    elif cidade_partida == 4: 
      cidade_partida = mapa.viana

    elif cidade_partida == 5: 
      cidade_partida = mapa.guarapari

    elif cidade_partida == 6: 
      cidade_partida = mapa.fundao

    elif cidade_partida == 7: 
      cidade_partida = mapa.domingosMartins

    elif cidade_partida == 8: 
      cidade_partida = mapa.marechalFloriano

    elif cidade_partida == 9: 
      cidade_partida = mapa.pedraAzul

    elif cidade_partida == 10: 
      cidade_partida = mapa.vendaNovaDoImigrante

    elif cidade_partida == 11: 
      cidade_partida = mapa.castelo

    elif cidade_partida == 12: 
      cidade_partida = mapa.santaLeopoldina

    elif cidade_partida == 13: 
      cidade_partida = mapa.anchieta

    elif cidade_partida == 14: 
      cidade_partida = mapa.cachoeiroDoItapemirim

    elif cidade_partida == 15: 
      cidade_partida = mapa.aracruz

    elif cidade_partida == 16: 
      cidade_partida = mapa.santaTeresa

    elif cidade_partida == 17: 
      cidade_partida = mapa.joaoNeiva

    # busca_aestrela = AEstrela(cidade_partida) - vai ser a busca gulosa
    # busca_aestrela.buscar(mapa.vilaVelha)

    break

  elif (opcao == 2):

    print(" ")
    print("Você escolheu a Busca AEstrela.")
    print(" ")
    print("O destino padrão é Vila Velha.")
    print(" ")
    print("1 - Vitória")
    print("2 - Serra")
    print("3 - Cariacica")
    print("4 - Viana")
    print("5 - Guarapari")
    print("6 - Fundão")
    print("7 - Domingos Martins")
    print("8 - Marechal Floriano")
    print("9 - Pedra Azul")
    print("10 - Venda Nova do Imigrante")
    print("11 - Castelo")
    print("12 - Santa Leopoldina")
    print("13 - Anchieta")
    print("14 - Cachoeiro do Itapemirim")
    print("15 - Aracruz")
    print("16 - Santa Teresa")
    print("17 - João Neiva")
    print(" ")
    cidade_partida = int(input("Escolha é a cidade de partida: "))

    if cidade_partida == 1: 
      cidade_partida = mapa.vitoria

    elif cidade_partida == 2: 
      cidade_partida = mapa.serra
    
    elif cidade_partida == 3: 
      cidade_partida = mapa.cariacica

    elif cidade_partida == 4: 
      cidade_partida = mapa.viana

    elif cidade_partida == 5: 
      cidade_partida = mapa.guarapari

    elif cidade_partida == 6: 
      cidade_partida = mapa.fundao

    elif cidade_partida == 7: 
      cidade_partida = mapa.domingosMartins

    elif cidade_partida == 8: 
      cidade_partida = mapa.marechalFloriano

    elif cidade_partida == 9: 
      cidade_partida = mapa.pedraAzul

    elif cidade_partida == 10: 
      cidade_partida = mapa.vendaNovaDoImigrante

    elif cidade_partida == 11: 
      cidade_partida = mapa.castelo

    elif cidade_partida == 12: 
      cidade_partida = mapa.santaLeopoldina

    elif cidade_partida == 13: 
      cidade_partida = mapa.anchieta

    elif cidade_partida == 14: 
      cidade_partida = mapa.cachoeiroDoItapemirim

    elif cidade_partida == 15: 
      cidade_partida = mapa.aracruz

    elif cidade_partida == 16: 
      cidade_partida = mapa.santaTeresa

    elif cidade_partida == 17: 
      cidade_partida = mapa.joaoNeiva

    busca_aestrela = AEstrela(mapa.aracruz)
    busca_aestrela.buscar(mapa.vilaVelha)
    break