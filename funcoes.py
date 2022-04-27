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