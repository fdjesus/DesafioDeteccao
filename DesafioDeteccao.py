#Bibliotecas
import numpy as np

#Constantes
limite = 3

#Classe que detecte valores fora do perfil da maioria dos valores já inseridos anteriormente
class DetectaAnomalia:
      #Construtor
      def __init__(self):
          self.lista_valores = []
          self.media = 0
          self.desvio_padrao = 0

      #Metodo para incluir valores na lista (verifica antes se valor esta dentro do perfil da maioria dos valores já inseridos anteriormente)
      def setValorLista(self, valor):
          if len(self.lista_valores) in (0,1):
             self.lista_valores.append(valor)
             return "ok"
          else:
             media = self.getMedia()
             desvio_padrao = self.getDesvioPadrao()
             if desvio_padrao == 0:
                self.lista_valores.append(valor)
                return "ok"
             else:
                zscore = (valor - media) / desvio_padrao
                if np.abs(zscore) > limite:
                   return "Valor fora do espectro já recebido"
                else:
                   self.lista_valores.append(valor)
                   return "ok"

      #Metodo para consultar a media da lista de valores
      def getMedia(self):
          self.media = np.mean(self.lista_valores)
          return self.media 

      #Metodo para consultar o desvio padrao da lista de valores
      def getDesvioPadrao(self):
          self.desvio_padrao = np.std(self.lista_valores)
          return self.desvio_padrao

#Programa Principal
sair = False
contador = 1
desafioDeteccao = DetectaAnomalia()
print("Digite 'sair' para finalizar o programa")
while(sair == False):
      valor = raw_input("[{}]Input: ".format(contador))
      if valor == "sair":
         sair = True
      else:
         try:
             numero = int(valor)
             if numero < 0:
                print("Digite um valor inteiro positivo")
             else:
                retorno_deteccao = desafioDeteccao.setValorLista(numero)
                print("[{}]Output: ".format(contador) + retorno_deteccao)
                print("")
                contador = contador + 1
         except ValueError:
              print("Digite 'sair' ou um valor inteiro positivo")
