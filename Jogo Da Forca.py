# print("--------\n|      |\n|      |\n|\n|\n|\n")
# print("--------\n|      |\n|      |\n|      O\n|\n|\n")
# print("--------\n|      |\n|      |\n|      O\n|      |\n|\n")
# print("--------\n|      |\n|      |\n|      O\n|     /|\n|\n")
# print("--------\n|      |\n|      |\n|      O\n|     /|\ \n|\n")
# print("--------\n|      |\n|      |\n|      O\n|     /|\ \n|      / \n")
# print("--------\n|      |\n|      |\n|      O\n|     /|\ \n|     / \ \n")

import random
#níveis da forca pré-desenhado em uma lista
forcaNiveis = ["--------\n|      |\n|      |\n|\n|\n|\n","--------\n|      |\n|      |\n|      O\n|\n|\n","--------\n|      |\n|      |\n|      O\n|      |\n|\n","--------\n|      |\n|      |\n|      O\n|     /|\n|\n","--------\n|      |\n|      |\n|      O\n|     /|\ \n|\n","--------\n|      |\n|      |\n|      O\n|     /|\ \n|     / \n","--------\n|      |\n|      |\n|      O\n|     /|\ \n|     / \ \n"]

escolha = "1" #Escolha do usuário para sair do loop

#Definindo as palavras a serem escolhidas
palavrasAnimais = ["arara","gato","rato","cachorro","baleia","elefante","rinoceronte","porco","galinha","vaca","boi","papagaio","hamster","macaco","capivara","girafa","camelo","pato","ganso"] 
palavrasComidas = ["arroz","feijao","batata","frango","carne","macarrao","lasanha","pizza","hamburger","esfirra","coxinha","miojo"]
palavrasFrutas = ["laranja","uva","pera","pitaya","acerola","limao","maracuja","morango","guarana"]

#lista com os temas
temas = [palavrasAnimais,palavrasComidas,palavrasFrutas]
temasUser = ["Animais","Comidas","Frutas"]
temaEscolhido=None

while escolha=="1": #loop para repetir o jogo

    qtdDicas=3 #valor de quantidades de dicas disponíveis

    contTema=0 #contador do indice do tema
    print("Escolha seu tema") #pedindo o tema para o usuário
    for i in temasUser:
        contTema+=1
        print(f"{contTema} - {i}")
    print(f"{contTema+1} - Aleatório")

    temaEscolha = int(input())
    verifyEscolha=False
    while verifyEscolha==False: #verificando se o tema está certo, para não ocorrer erros no código
        if temaEscolha<=0 or temaEscolha>len(temas)+1:
            contTema=0
            print("Escolha seu tema")
            for i in temasUser:
                contTema+=1
                print(f"{contTema} - {i}")
            print(f"{contTema+1} - Aleatório")
            print("\n Digite um valor valor válido \n")
            temaEscolha = int(input())
        else:
            verifyEscolha=True

    if temaEscolha==contTema+1:
        temaEscolhido=random.choice(temas) #sistema de aletorizar temas
    else:
        temaEscolhido=temas[temaEscolha-1]
    

    palavraCriptografada = [] #Definindo a palavra criptografada

    palavraCerta = random.choice(temaEscolhido).upper() #Escolhendo a palavra aleátoria
    palavraCriptografada = "_ "*len(palavraCerta) #Definindo a palavra criptografada com _ para representar as letras

    print(forcaNiveis[0]) #Desenhando a forca
    print(f"Tema: {temasUser[temas.index(temaEscolhido)]}") #escrevendo o tema
    print(palavraCriptografada) #Mostrando a quantidade de letras

    listPalavraCriptografada=[] #Lista para troca de valores da palavra

    for letra in palavraCriptografada: #Forma de transformar palavra em lista ordenada
        listPalavraCriptografada.append(letra) 

    erros=0 #definindo os erros, para finalizar o jogo ao passar de 6

    letrasChutadas =[]

    while erros<=6:
        LetraChute = input("Digite a letra que quer chutar (Se quiser uma Dica digite 'Dica')\n").upper() #Pedindo a input da letra
        chuteCerto = False #se a letra chutada está dentro dos conformes
        dicaCerta=False #se a dica pode ser feita
        while chuteCerto==False: #repetição para para digitar apenas uma letra
            if LetraChute=="DICA": #sistemas de dicas
                if qtdDicas>0:
                    LetraChute=random.choice(palavraCerta) 
                    while dicaCerta==False:
                        if LetraChute in letrasChutadas:
                            LetraChute=random.choice(palavraCerta)
                        else:
                            dicaCerta=True
                            erros+=1
                            qtdDicas-=1
                            chuteCerto=True
                else:
                    print("Você já usou todas as dicas!")
                    LetraChute = input("Digite a letra que quer chutar (Se quiser uma Dica digite 'Dica')\n").upper()
            else:
                if len(LetraChute)==1:
                    if LetraChute in letrasChutadas:
                        print("Digite uma letra que não foi usada!")
                        LetraChute = input("Digite a letra que quer chutar (Se quiser uma Dica digite 'Dica')\n").upper()
                    else:
                        chuteCerto=True
                else:
                    print("Digite apenas uma letra!")
                    LetraChute = input("Digite a letra que quer chutar (Se quiser uma Dica digite 'Dica')\n").upper()

        letrasChutadas.append(LetraChute)

        indexLetrasCertas = [] #index das letras que estão corretas
        contLetra=0 #contador de letras da palavra

        if LetraChute in palavraCerta: #Vendo se a letra escrita está na palavra

            for letra in palavraCerta: #Contando cada letra da palavra certa

                if LetraChute==letra: #se a letra do cute for igual, coloca na lista de letras certas
                    indexLetrasCertas.append(contLetra)
                contLetra+=1

            contLetraCerta=0 #Contador de letras acertadas
            indexCriptografado=0 #contador de index da palavra criptografada


            for letra in palavraCriptografada: #alterando o valor da palavra criptografada para a quantidade certa
                
                if contLetraCerta in indexLetrasCertas and letra!=" ": #alterando se bater com o index das letras da palavra certa, se diferente de " "
                    listPalavraCriptografada[indexCriptografado]=LetraChute

                if letra!=" ": #se for espaço não altera 
                    contLetraCerta+=1
                indexCriptografado+=1 #aumentando contador do index da lista

            palavraCriptografada="" #transformando a palavra Criptografa em nada, para reformular ela novamente

            for i in listPalavraCriptografada: #reformulando a palavra criptografada
                palavraCriptografada+=i
                
            
        else: #else feito para falar que ele errou e aumentar os erros
            print("\nA letra não está na palavra\n")
            erros+=1

        if not erros>6: #verificação para não dar erro no "forcaNiveis[erros]"
            print(forcaNiveis[erros])
            print(palavraCriptografada)
            print(f"Letras já usadas: {letrasChutadas}")

        palavraCertaVerificando="" #palavra que está sendo verificada para ver se foi terminado, sem contar os erros
        for letra in palavraCriptografada:
            if letra!=" ":
                palavraCertaVerificando+=letra
        
        if palavraCertaVerificando==palavraCerta: #verificando se a palavra criptografada é igual a certa
            break

    if erros<=6: #verificando se perdeu por erros ou não
        print("\n ~~~ Acertou a palavra :) ~~~ \n")
    else:
        print("\n ~~~~ Errou a palavra :( ~~~ \n")
        print(f"A palavra certa era: {palavraCerta} \n")

    escolha = input("Você deseja Jogar novamente? \n 1 - Jogar Novamente \n 2 - Sair\n") #dando input para repetição

print("Programa Fechado")#mensagem para representar fim do programa

#V 1. Colocar mais temas do jogo (além de animais), e mais opções para cada tema (Talvez colocar um modo aleatório, escolhe temas aleatóriamente)
#2. Colocar sistema de dica