# aqui vamo colocar as funções pra puxar tudo de um import soh
import math as m          #  deixei a função math como m pra ser mais facil 
import random
def haversine(r, y1, k1, y2, k2):      # essa função calcula a distancia 
    # y1 e y2  = y cursiva estranho
    # k1 e k2 = y de ponta cabeça
    y1 = m.radians(y1)
    y2 = m.radians(y2)
    k1=m.radians(k1)
    k2 = m.radians(k2)
    q = m.sin((y2-y1)/2)**2 + m.cos(y2)*m.cos(y1)*m.sin((k2-k1)/2)**2
    raiz = m.sqrt(q)
    d = 2* r * m.asin(raiz)
    return d 
    # função ta certa e funcionando




def esta_na_lista(pais, lista):        #essa função verifica se determinado elemento esta em uma lista 
    for px in lista:
        if pais in px[0]:
            return True 
    return False
    # função ta certa e funcionando


def sorteia_pais(dici):         #função que sorteia um elemento de dicionario  
    lp = []
    for p in dici.keys():
        lp.append(p)
    return random.choice(lp)
    # função ta certa e funcionando



def sorteia_letra(palavra, lista_restritiva):      #função que sorteia uma letra em uma palavra que retira caracteres e as letras da lista restritiva 
    l = ['.', ',', '-', ';', ' ']
    nl = palavra
    for i in l:  
        nl = nl.replace(i, '')
    for i in lista_restritiva:
        nl =nl.replace(i,'')
    if nl == '':
        return nl
    else:
        p = random.choice(nl)
    return p 



def adiciona_em_ordem(pais, distancia, lp):    #função que deixa em ordem uma lista do maior para o menor (ela tah grande pq eu inverti ela pra deixar na ordem certa)
    ol = []
    for i in lp:
        oadd = [i[1], i[0]]
        ol.append(oadd)
    oadd = [distancia, pais]
    ol.append(oadd)
    ol.sort()
    lp =[]
    for lis in ol:
        lp.append([lis[1], lis[0]])
    print(lp)
    return lp



def normaliza(dici):       #função que  normaliza a base de dados 
    dp = {}
    for continente in dici:
        for pais in dici[continente]:
            dp[pais] = dici[continente][pais]
            dp[pais]["continente"] = continente 
    return dp