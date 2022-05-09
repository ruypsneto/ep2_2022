# aqui vamo importar as funções do arquivo 'funçoes' pra rodar o sistema

import funcoes as f 
from base_de_dados import dados
from base_de_dados import raio_terra
import termcolor 

 
logo = print('                       /////////////////////////////////\n                               INSPER PELO MUNDO\n                       /////////////////////////////////\n \n \n  \n \n \n ')
inicia_jogo = str(input('Iniciar Jogo[sim/nao]:'))

while inicia_jogo != 'sim':
    logo 
    inicia_jogo = str(input('Iniciar Jogo:'))




quer_jogar_novamente = True
jogo = True 
dados_convertidos = f.normaliza(dados)      # dados que vamos utilizar 
while quer_jogar_novamente == True:         # aqui vai deixar o jogo em loop ate que o jogador nao queira mais 
    tentativas = 20 
    pais_sorteado = f.sorteia_pais(dados_convertidos)
    lat_pais = dados_convertidos[pais_sorteado]['geo']['latitude']
    long_pais = dados_convertidos[pais_sorteado]['geo']['longitude']
    lista_registro_tentativas = []

    while jogo == True:        # aqui vai ser onde roda o jogo 
        # estrutura a pensar, tem um break pra n ferrar com o codigo mas depois tira 
        print('Voce tem', tentativas,'restantes')
        palpite = str(input('Qual seu palpite?')).lower()
        palpite = palpite.strip()

        while  palpite  not in dados_convertidos.keys():
            if palpite == 'dicas' or palpite == 'desisto':
                break
            print('invalido')
            palpite = str(input('Qual seu palpite?'))

        if palpite == 'dicas':
            n_dica = int(input('qual dica deseja?'))
            if n_dica == 1:
               a = dados_convertidos[pais_sorteado]['area']
               print('{0} km²'.format(a))
            elif n_dica == 2:
                p = dados_convertidos[pais_sorteado]['populacao']
                print('{0} habitantes'.format(p))
            elif n_dica == 3:
                c = dados_convertidos[pais_sorteado]['capital']
                letras_capital = []
                l_c =  f.sorteia_letra(c, letras_capital)
                print(l_c)
                letras_capital.append(l_c)
            elif n_dica == 4:
                cont = dados_convertidos[pais_sorteado]['continente']
                print('o continente é ', cont)
            elif n_dica == 5:
                b = dados_convertidos[pais_sorteado]['bandeira']
                for cor, qtd in b.items():
                    if qtd > 0:
                        print(cor)
            elif n_dica == 0:
                 palpite = str(input('Qual seu palpite?'))

                

        elif palpite == 'desisto':
            print('Voce esta nervoso? \n Perdeu por desistencia')
            break


        while  palpite  not in dados_convertidos.keys():
            if palpite == 'dicas' or palpite == 'desisto':
               palpite = str(input('Qual seu palpite?'))
            else: 
                print('invalido')
                palpite = str(input('Qual seu palpite?'))
        
        if tentativas <= 0:
            print('voce perdeu, nao te restam tentativas')
            break

        if palpite == pais_sorteado:
            
            print('Parabens voce venceu!!!!\n  \n  \n   ')
            print('Voce conseguio em {0}'.format(tentativas))
            break



        if palpite != 'dicas' and palpite != 'desisto':
            verifica_registro = f.esta_na_lista(palpite, lista_registro_tentativas)

            if verifica_registro == False:

                lat_palpite = dados_convertidos[palpite]['geo']['latitude']
                long_palpite = dados_convertidos[palpite]['geo']['longitude']  
                distancia = f.haversine(raio_terra, lat_palpite, lat_pais, long_palpite, long_pais)
                lista_registro_tentativas = f.adiciona_em_ordem(palpite, distancia, lista_registro_tentativas)
                
                for registro in lista_registro_tentativas:
                    if registro[1] <= 1000:
                        cor = 'green'

                    elif registro[1] <= 2000:
                        cor = 'red'

                    elif registro[1] <= 5000:
                        cor = 'blue'
                    
                    elif  registro[1] <= 8000:
                        cor= 'cyan'
                    elif registro[1] <= 10000:
                        cor = 'yellow'

                    elif registro[1] > 10000:
                        cor = 'white'
                    
                    info_a_printar = '{1} ------ {0:.1f} Km'.format(registro[1], registro[0])
                    print(termcolor.colored(info_a_printar, cor))



                
                tentativas -= 1
    


    quer_jogar = str(input('Quer jogar novamente?[sim/nao]  '))
    while quer_jogar != 'sim' and quer_jogar != 'nao':
        print('invalido') 
        quer_jogar = str(input('Quer jogar novamente?[sim/nao]  '))
    if quer_jogar == 'sim':
            jogo == True 
    else:
        print('Obrigado por jogar!!!')
        quer_jogar_novamente = False
