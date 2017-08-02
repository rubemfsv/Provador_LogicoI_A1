print("INSTRUÇOES :\n1 - Digite o predicado a ser verficado\nExemplo: Q\n")

p = input("") #Predicado a ser verificado

list = []

print ("\n2 - Digite as proposicoes e para indicar o termino digite 0\nExemplo:\nP -> Q\nP\n0\n\nUtilize: '->'(implica), '~'(negacao), v(letra v, representando o 'OU')).")

while(True):
    proposicao = input("")

    if(proposicao.__eq__('0')):
        break;

    list.append(proposicao)  #adiciona na lista

#aprovador lógico
tamanho = list.__len__()
w, h = 100, 100;
Matrix = [[0 for x in range(w)] for y in range(h)]

i = 0
#y = 0
#y1 = 0
#y2 = 0
while i < tamanho:
    if(list[i].__eq__(p)):
        #y = -1
        print(p + " VERDADEIRO")
    if(list[i].__len__() > 2):
        buffer241 = list[i].split()
        buffer24 = buffer241[0:1] #Pega o primeiro elemento da proposição
        a = buffer241[2:3] #Pega ultimo elemento
        if(a.__eq__('-')):
            buffer2 = buffer241[5:list[i].__len__()]
            j = 0
            while j < tamanho:
                if((Matrix[i][j] != 1)):
                    if(list[j].__eq__(buffer24)):
                        Matrix[i][j] = 1
                        #i = 0
                        #y += 1
                        #list.append(buffer2)
                        #y1 = i + 1
                        #y2 = j + 1
                        b = list[i]
                        print("O prédicado é " + p + " e a(s) proposições é/são a(s) seguinte(s): ")
                        print(list)
                        print("Por Modus Ponens ")
                        print(list[j])
                        print( "e o prédicado provado como verdadeiro é " + p)
                        break
            j += 1
    i += 1
