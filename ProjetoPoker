import random

cartasBaralhoOfc = ["2♦","2♠","2♥","2♣","3♦","3♠","3♥","3♣","4♦","4♠","4♥","4♣","5♦","5♠","5♥","5♣","6♦","6♠","6♥","6♣","7♦","7♠","7♥","7♣","8♦","8♠","8♥","8♣","9♦","9♠","9♥","9♣","10♦","10♠","10♥","10♣","J♦","J♠","J♥","J♣","Q♦","Q♠","Q♥","Q♣","K♦","K♠","K♥","K♣","A♦","A♠","A♥","A♣"]
cartasBaralhoRest = cartasBaralhoOfc

algarismos = ["0","1","2","3","4","5","6","7","8","9"]

listaRTF =["10","J","Q","K","A"]

class players:
    
    def __init__(self,cardsReal,cards,iHigh,iPar,i2Par,iTrio,iStraight,iFlush,iFullHouse,iPoker,iSF,iRTF,iOuro,iEspada,iCopas,iPaus):
        self.cardsReal: list = cardsReal
        self.cards: list = cards
        self.iHigh = iHigh
        self.iPar = iPar
        self.i2Par = i2Par
        self.iTrio = iTrio
        self.iStraight = iStraight
        self.iFlush = iFlush
        self.iFullHouse = iFullHouse
        self.iPoker = iPoker
        self.iSF = iSF
        self.iRTF = iRTF
        self.iOuro = iOuro
        self.iEspada = iEspada
        self.iCopas = iCopas
        self.iPaus = iPaus

def novaCarta(player): #Adiciona nova carta ao player, coloca o valor na lista de Card e o naipe no seu respectivo contador, e as cartas reais na lista visual
    cartaNova = random.choice(cartasBaralhoRest)
    cartasBaralhoRest.remove(cartaNova)
    player.cardsReal.append(cartaNova)
    for caractere in cartaNova:
        if caractere in algarismos:
            print("Placeholder")


def verifyMao(player):
    if player.iOuro>=5 or player.iPaus>=5 or player.iEspada>=5 or player.iCopas>=5:
        if listaRTF in player.cards:
            return print("RTF")

player1= players([],[],None,None,None,None,None,None,None,None,None,None)
player2= players([],[],None,None,None,None,None,None,None,None,None,None)
player3= players([],[],None,None,None,None,None,None,None,None,None,None)
player4= players([],[],None,None,None,None,None,None,None,None,None,None)
player5= players([],[],None,None,None,None,None,None,None,None,None,None)
player6= players([],[],None,None,None,None,None,None,None,None,None,None)
player7= players([],[],None,None,None,None,None,None,None,None,None,None)
player8= players([],[],None,None,None,None,None,None,None,None,None,None)

listPlayersOriginal = [player1,player2,player3,player4,player5,player6,player7,player8]
listPlayers = []
verifyQtdPlayers =False

qtdPlayers = int(input("Quantos jogadores irão jogar? (Min:2 | Max: 8)\n"))

while verifyQtdPlayers==False:
    if qtdPlayers>8:
        print("Escreva um quantidade menor que 8!\n")
        qtdPlayers = int(input("Quantos jogadores irão jogar? (Max: 8)\n"))
    else:
        if qtdPlayers<2:
            print("Escreva uma quantiade maior que 1")
            qtdPlayers = int(input("Quantos jogadores irão jogar? (Max: 8)\n"))
        else:
            print(f"{qtdPlayers} Jogadores em jogo")
            verifyQtdPlayers=True
            
for i in range(0,qtdPlayers):
    listPlayers.append(listPlayersOriginal[i])
print(listPlayers)

    

        

# print(len(cartasBaralhoRest))

# cartasP1= []
# cartasP1.append(random.choice(cartasBaralhoRest))
# cartasBaralhoRest.remove(cartasP1[0])
# cartasP1.append(random.choice(cartasBaralhoRest))
# cartasBaralhoRest.remove(cartasP1[1])

# print(f"sua mão é {cartasP1[0]} e {cartasP1[1]}")



#1. Função que verifica mãos do poker
