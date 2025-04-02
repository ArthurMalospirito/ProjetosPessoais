import random

from collections import Counter

cartasBaralhoOfc = ["2♦","2♠","2♥","2♣","3♦","3♠","3♥","3♣","4♦","4♠","4♥","4♣","5♦","5♠","5♥","5♣","6♦","6♠","6♥","6♣","7♦","7♠","7♥","7♣","8♦","8♠","8♥","8♣","9♦","9♠","9♥","9♣","10♦","10♠","10♥","10♣","J♦","J♠","J♥","J♣","Q♦","Q♠","Q♥","Q♣","K♦","K♠","K♥","K♣","A♦","A♠","A♥","A♣"]
cartasBaralhoRest = cartasBaralhoOfc

algarismos = ["0","1","2","3","4","5","6","7","8","9"]

listaRTF =["10","J","Q","K","A"]
listaStraight=[["A","2","3","4","5"],["6","2","3","4","5"],["6","7","3","4","5"],["6","7","8","4","5"],["6","7","8","9","5"],["6","7","8","9","10"],["J","7","8","9","10"],["J","Q","8","9","10"],["J","Q","K","9","10"],["J","Q","K","A","10"]]

class players:
    
    def __init__(self,cardsReal,cards,iOuro,iEspada,iCopas,iPaus,mao,iMaiorQtd,iSegundaMaiorQtd):
        self.cardsReal: list = cardsReal
        self.cards: list = cards
        self.iOuro: int = iOuro
        self.iEspada: int = iEspada
        self.iCopas: int = iCopas
        self.iPaus: int = iPaus
        self.mao = mao
        self.iMaiorQtd: list = iMaiorQtd
        self.iSegundaMaiorQtd: list = iSegundaMaiorQtd

altenadorNaipe = False

#newCard = random.choice(cartasBaralhoRest)
#cartasBaralhoRest.remove(newCard)
def novaCarta(player,carta): #Adiciona nova carta ao player, coloca o valor na lista de Card e o naipe no seu respectivo contador, e as cartas reais na lista visual
    cartaNova = carta
    player.cardsReal.append(cartaNova)
    for caractere in cartaNova:
        if caractere in algarismos:
            valorCartaAdd+=caractere
        else:
            player.cards.append(valorCartaAdd)
            match caractere:
                case "♦":
                    player.iOuro+=1
                case "♠":
                    player.iEspada+=1
                case "♥":
                    player.iCopas+=1
                case "♣":
                    player.iPaus+=1


def verifyMao(player):
    itensRepetidos = Counter(player.cards).most_common(2)
    player.iMaiorQtd = itensRepetidos[0] # Item / Quantidade
    player.iSegundoMaiorQtd = itensRepetidos[1] # Item / Quantidade

    if player.iOuro>=5 or player.iPaus>=5 or player.iEspada>=5 or player.iCopas>=5:
        if all(elem in player.cards for elem in listaRTF):
            return print("RTF")
        else:
            for i in range(0,len(listaStraight)):
                if all(elem in player.cards for elem in listaStraight[i]):
                    return print("SF")
        return print("Flush")
    else:
        print("Resto") #CONTINUAR AQUII ! ! ! ! ! ! ! ! ! ! ! !
    
player1 = players([],[],0,0,0,0,[],[])
player1.iOuro=5

#player1.cards=["10","J","Q","K","A","2","A"] #RTF
#player1.cards=["2","3","4","5","6","2","10"] #SF
#player1.cards=["A","3","7","J","5","9","Q"] #Flush
player1.cards=["8","8","8","8","4","7","A"] #Poker

verifyMao(player1)


        

# player1= players([],[],None,None,None,None,None,None,None,None,None,None)
# player2= players([],[],None,None,None,None,None,None,None,None,None,None)
# player3= players([],[],None,None,None,None,None,None,None,None,None,None)
# player4= players([],[],None,None,None,None,None,None,None,None,None,None)
# player5= players([],[],None,None,None,None,None,None,None,None,None,None)
# player6= players([],[],None,None,None,None,None,None,None,None,None,None)
# player7= players([],[],None,None,None,None,None,None,None,None,None,None)
# player8= players([],[],None,None,None,None,None,None,None,None,None,None)

# listPlayersOriginal = [player1,player2,player3,player4,player5,player6,player7,player8]
# listPlayers = []
# verifyQtdPlayers =False

# qtdPlayers = int(input("Quantos jogadores irão jogar? (Min:2 | Max: 8)\n"))

# while verifyQtdPlayers==False:
#     if qtdPlayers>8:
#         print("Escreva um quantidade menor que 8!\n")
#         qtdPlayers = int(input("Quantos jogadores irão jogar? (Max: 8)\n"))
#     else:
#         if qtdPlayers<2:
#             print("Escreva uma quantiade maior que 1")
#             qtdPlayers = int(input("Quantos jogadores irão jogar? (Max: 8)\n"))
#         else:
#             print(f"{qtdPlayers} Jogadores em jogo")
#             verifyQtdPlayers=True
            
# for i in range(0,qtdPlayers):
#     listPlayers.append(listPlayersOriginal[i])
# print(listPlayers)

    

        

# print(len(cartasBaralhoRest))

# cartasP1= []
# cartasP1.append(random.choice(cartasBaralhoRest))
# cartasBaralhoRest.remove(cartasP1[0])
# cartasP1.append(random.choice(cartasBaralhoRest))
# cartasBaralhoRest.remove(cartasP1[1])

# print(f"sua mão é {cartasP1[0]} e {cartasP1[1]}")



#1. Função que verifica mãos do poker
