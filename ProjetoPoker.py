import random

from collections import Counter

cartasBaralhoOfc = ["2♦","2♠","2♥","2♣","3♦","3♠","3♥","3♣","4♦","4♠","4♥","4♣","5♦","5♠","5♥","5♣","6♦","6♠","6♥","6♣","7♦","7♠","7♥","7♣","8♦","8♠","8♥","8♣","9♦","9♠","9♥","9♣","10♦","10♠","10♥","10♣","J♦","J♠","J♥","J♣","Q♦","Q♠","Q♥","Q♣","K♦","K♠","K♥","K♣","A♦","A♠","A♥","A♣"]
cartasBaralhoRest = cartasBaralhoOfc

algarismos = ["0","1","2","3","4","5","6","7","8","9","J","Q","K","A"]

ordemCartas=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

listaRTF =["10","J","Q","K","A"]
listaStraight=[["A","2","3","4","5"],["6","2","3","4","5"],["6","7","3","4","5"],["6","7","8","4","5"],["6","7","8","9","5"],["6","7","8","9","10"],["J","7","8","9","10"],["J","Q","8","9","10"],["J","Q","K","9","10"],["J","Q","K","A","10"]]

class players:
    
    def __init__(self,cardsReal,cards,iOuro,iEspada,iCopas,iPaus,mao,iMaiorQtd,nome,stack,funcao,aposta):
        self.cardsReal: list = cardsReal #Cartas de forma bonitinha:  2♦, 9♠...
        self.cards: list = cards #Valor númerico das cartas: A,2,3,4...Q,K
        self.iOuro: int = iOuro #contador do naipe
        self.iEspada: int = iEspada #contador do naipe
        self.iCopas: int = iCopas #contador do naipe
        self.iPaus: int = iPaus #contador do naipe
        self.mao: list = mao #mão é uma lista: [0]="FullHouse",[1]=3(primeiro critério da mão),[2]=6(Segundo critério da mão)
        self.iMaiorQtd: list = iMaiorQtd #Valor de maior quantidade: [0]=Item mais repetido, [1]=Segundo item mais repetido
        self.nome: str = nome
        self.stack: int =stack
        self.funcao: str = funcao
        self.aposta: int = aposta


def novaCarta(player,carta): #Adiciona nova carta ao player, coloca o valor na lista de Card e o naipe no seu respectivo contador, e as cartas reais na lista visual
    valorCartaAdd =""
    cartaNova = carta
    if len(player.cardsReal)<=2:
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
    player.iMaiorQtd = itensRepetidos # Item / Quantidade


    if player.iOuro>=5 or player.iPaus>=5 or player.iEspada>=5 or player.iCopas>=5:

        RSF=False
        SF=False
        
        if all(elem in player.cards for elem in listaRTF):
            player.mao.insert(0,"RSF")
            #return print("Royal Straight Flush")
            RSF=True

        else:
            for i in range(0,len(listaStraight)):
                if all(elem in player.cards for elem in listaStraight[i]):
                    player.mao.insert(0,"SF")
                    player.mao.insert(1,i)
                    #return print("Straight Flush")
                    SF=True
                
        if RSF==False and SF==False:
            player.mao.insert(0,"flush")
            cartasDoFlush=[]
            if player.iOuro>=5:
                naipeTemp = "♦"
            if player.iPaus>=5:
                naipeTemp="♣"
            if player.iCopas>=5:
                naipeTemp="♥"
            if player.iEspada>=5:
                naipeTemp="♠"
            for carta in player.cardsReal:
                for letra in carta:
                    if letra==naipeTemp:
                        cartasDoFlush.append(carta)
            player.mao.insert(1,cartasDoFlush)
            #return print("Flush")
    
    else: 
        
        straight=False

        for i in range(0,len(listaStraight)):
            if all(elem in player.cards for elem in listaStraight[i]):
                player.mao.insert(0,"straight")
                player.mao.insert(1,i)
                #return print("Straight")
                straight=True
            
        if straight==False:
            if player.iMaiorQtd[0][1]>=4:
                player.mao.insert(0,"poker")
                player.mao.insert(1,player.iMaiorQtd[0][0])
                #return print("Poker")
            
            elif player.iMaiorQtd[0][1]>=3 and player.iMaiorQtd[1][1]>=2:
                player.mao.insert(0,"FH")
                player.mao.insert(1,player.iMaiorQtd[0][0])
                player.mao.insert(2,player.iMaiorQtd[1][0])
                #return print("Full House")
            
            elif player.iMaiorQtd[0][1]>=3:
                player.mao.insert(0,"trio")
                player.mao.insert(1,player.iMaiorQtd[0][0])
                #return print("Trio")
            
            elif player.iMaiorQtd[0][1]>=2 and player.iMaiorQtd[1][1]>=2:
                player.mao.insert(0,"2par")
                player.mao.insert(1,player.iMaiorQtd[0][0])
                player.mao.insert(2,player.iMaiorQtd[1][0])
                #return print("Dois Pares")
            
            elif player.iMaiorQtd[0][1]>=2:
                player.mao.insert(0,"par")
                player.mao.insert(1,player.iMaiorQtd[0][0])
                #return print("Par")
            
            else:
                player.mao.insert(0,"HC")
                HC=player.cards[0]
                for carta in player.cards:
                    if ordemCartas.index(carta)>ordemCartas.index(HC):
                        HC = carta
                player.mao.insert(1,HC)
                #return print("High Card")
    
    

player1 = players([],[],0,0,0,0,[],[],"",1000,"",0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Teste rápido para verificar mãos ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#cartasParaAdd=["10♣","J♣","Q♣","K♣","A♣","2♥","5♦"] #RTF
#cartasParaAdd=["2♥","3♥","4♥","5♥","6♥","2♦","10♣"] #SF
#cartasParaAdd=["8♣","8♥","8♠","8♦","4♣","7♥","A♦"] #Poker
#cartasParaAdd=["8♥","8♠","8♦","4♣","4♠","7♣","A♦"] #Full House
#cartasParaAdd=["A♦","3♦","7♦","J♦","5♦","9♥","Q♠"] #Flush
#cartasParaAdd=["10♣","J♥","Q♠","K♦","4♣","7♥","A♠"] #Straight
#cartasParaAdd=["8♣","8♥","8♠","2♦","4♣","7♥","A♦"] #Trio
#cartasParaAdd=["8♣","8♥","5♣","4♥","4♠","7♦","A♦"] #Dois Pares
#cartasParaAdd=["8♣","8♠","6♥","Q♦","4♣","7♥","A♠"] #Par
#cartasParaAdd=["2♣","5♥","8♠","A♦","4♣","7♥","Q♠"] #High Card

# for i in cartasParaAdd:
#     novaCarta(player1,i)

# for i in range(0,7):
#     newCard = random.choice(cartasBaralhoRest)
#     cartasBaralhoRest.remove(newCard)
#     novaCarta(player1,newCard)

# print(player1.cardsReal)
# verifyMao(player1)
# print(player1.mao)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ VERIFICADOR DE MUTIPLA QUANTIDADE DE VEZES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# contadorNecessidade=0
# while True:
#     player1.cardsReal=[]
#     player1.cards=[]
#     player1.iOuro=0
#     player1.iEspada=0
#     player1.iCopas=0
#     player1.iPaus=0
#     player1.mao=[]
#     player1.iMaiorQtd=[]
#     cartasBaralhoRest = ["2♦","2♠","2♥","2♣","3♦","3♠","3♥","3♣","4♦","4♠","4♥","4♣","5♦","5♠","5♥","5♣","6♦","6♠","6♥","6♣","7♦","7♠","7♥","7♣","8♦","8♠","8♥","8♣","9♦","9♠","9♥","9♣","10♦","10♠","10♥","10♣","J♦","J♠","J♥","J♣","Q♦","Q♠","Q♥","Q♣","K♦","K♠","K♥","K♣","A♦","A♠","A♥","A♣"]
#     for i in range(0,7):
#         newCard = random.choice(cartasBaralhoRest)
#         cartasBaralhoRest.remove(newCard)
#         novaCarta(player1,newCard)

#     print(player1.cardsReal)
#     verifyMao(player1)
#     print(player1.mao)
#     if player1.mao[0]=="RSF":
#         break
#     contadorNecessidade+=1
# print(contadorNecessidade)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ JOGO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#player1 = players([],[],0,0,0,0,[],[])
player2 = players([],[],0,0,0,0,[],[],"",1000,"",0)
player3 = players([],[],0,0,0,0,[],[],"",1000,"",0)
player4 = players([],[],0,0,0,0,[],[],"",1000,"",0)
player5 = players([],[],0,0,0,0,[],[],"",1000,"",0)
player6 = players([],[],0,0,0,0,[],[],"",1000,"",0)
player7 = players([],[],0,0,0,0,[],[],"",1000,"",0)
player8 = players([],[],0,0,0,0,[],[],"",1000,"",0)

listPlayersOriginal = [player1,player2,player3,player4,player5,player6,player7,player8]
ofcOrdemPlayers = [0,1,2,3,4,5,6,7]
ordemPlayers = []
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
    ordemPlayers.append(ofcOrdemPlayers[i])
    listPlayers[i].nome = input(f"Digite o nome do player{i+1}:\n")

#while acabar jogo
contadorRodada=1
#comecarRound = input(f"Começar Rodada {contadorRodada}?\n").lower()

for player in listPlayers:
    for i in range(0,2):
        cartaNova = random.choice(cartasBaralhoRest)
        cartasBaralhoRest.remove(cartaNova)
        novaCarta(player,cartaNova)
mesa =[]
# input("Mostrar primeira mão?\n")
# for player in listPlayers:
#     print(f"{player.nome}, Sua mão é:")
#     print(player.cardsReal)
#     input("Mostrar próxima mão?\n")
#     print("\n\n\n\n\n\n\n\n\n\n\n")
#     input("Mostrar próxima mão?\n") if listPlayers.index(player)<len(listPlayers)-1 else print()
    
input("Começar Rodada?\n")
listPlayers[ordemPlayers[0]].funcao = "SB"
listPlayers[ordemPlayers[1]].funcao = "BB" 
input(f"Mostrar {listPlayers[ordemPlayers[0]].nome}?\n")
maiorAposta = 0
pot = 0
for i in ordemPlayers:
    if i==0:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"{listPlayers[ordemPlayers[i]].nome}, você é o Small Blind\n")
        print(f"{listPlayers[ordemPlayers[i]].cardsReal}\n")
        print("A aposta mínima da mesa inicial é 5\n")
        print(f"O pote é: {pot}\n")
        #listPlayers[ordemPlayers[i]].aposta
        apostaTemp = int(input("Digite sua aposta:\n"))
        apostaCerta=False
        while apostaCerta==False:
            if apostaTemp<5:
                print("A aposta deve ser maior ou igual a 5")
                apostaTemp = int(input("Digite sua aposta:\n"))
            else:
                apostaCerta=True
        listPlayers[ordemPlayers[i]].aposta = apostaTemp
        maiorAposta = apostaTemp
        pot+=apostaTemp
    elif i==1:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"Mostrar {listPlayers[ordemPlayers[i]].nome}?\n")
        print(f"{listPlayers[ordemPlayers[i]].nome}, você é o Big Blind\n")
        print(f"{listPlayers[ordemPlayers[i]].cardsReal}\n")
        print(f"A aposta mínima da mesa é {maiorAposta*2}\n")
        print(f"O pote é: {pot}\n")
        apostaTemp = int(input("Digite sua aposta:\n"))
        apostaCerta=False
        while apostaCerta==False:
            if apostaTemp<maiorAposta*2:
                print(f"A aposta deve ser maior ou igual a {maiorAposta*2}")
                apostaTemp = int(input("Digite sua aposta:\n"))
            else:
                apostaCerta=True
        listPlayers[ordemPlayers[i]].aposta = apostaTemp
        maiorAposta = apostaTemp
        pot+=apostaTemp
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"Mostrar {listPlayers[ordemPlayers[i]].nome}?\n")
        print(f"{listPlayers[ordemPlayers[i]].nome}, É a sua Vez\n")
        print(f"{listPlayers[ordemPlayers[i]].cardsReal}\n")
        print(f"A aposta mínima da mesa é {maiorAposta}\n")
        print(f"O pote é: {pot}\n")
        apostaTemp = int(input("Digite sua aposta:\n"))
        apostaCerta=False
        while apostaCerta==False:
            if apostaTemp<maiorAposta:
                print(f"A aposta deve ser maior ou igual a {maiorAposta}")
                apostaTemp = int(input("Digite sua aposta:\n"))
            else:
                apostaCerta=True
        listPlayers[ordemPlayers[i]].aposta = apostaTemp
        maiorAposta = apostaTemp
        pot+=apostaTemp
    

#1. Função que verifica desempate, mesma coisa da mão normal, mas ignora a mão inicial e vai na segunda.
