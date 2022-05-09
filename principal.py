# aqui vamo importar as funções do arquivo 'funçoes' pra rodar o sistema
import funcoes as f 
from base_de_dados import dados
from base_de_dados import raio_terra

inicia_jogo = str(input('Iniciar Jogo[sim/nao]:'))

while inicia_jogo != 'sim':
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
        palpite = str(input('Qual seu palpite?'))
        
        if palpite == 'dicas':
            # vai para mercado de diacas
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


                

            

        
        while palpite not in dados_convertidos.keys():
            print('invalido')
            palpite = str(input('Qual seu palpite?'))

        tentativas -= 1
        if tentativas <= 0:
            print('voce perdeu, nao te restam tentativas')

        if palpite == pais_sorteado:
            
            print('Parabens voce venceu!!!! ')
            print('voce conseguiu em {0}'.format(tentativas))
            break

        else:
            verifica_registro = f.esta_na_lista(palpite, lista_registro_tentativas)
        
            if verifica_registro == False:

                lat_palpite = dados_convertidos[palpite]['geo']['latitude']
                long_palpite = dados_convertidos[palpite]['geo']['longitude']  
                distancia = f.haversine(raio_terra, lat_palpite, lat_pais, long_palpite, long_pais)
                lista_registro_tentativas = f.adiciona_em_ordem(palpite, distancia, lista_registro_tentativas)
                print(lista_registro_tentativas)
















        break 


    quer_jogar = str(input('Quer jogar novamente?[sim/nao]  '))
    while quer_jogar != 'sim' and quer_jogar != 'nao':
        print('invalido') 
        quer_jogar = str(input('Quer jogar novamente?[sim/nao]  '))
    if quer_jogar == 'sim':
            jogo == True 
    else:
        print('Obrigado por jogar!!!')
        quer_jogar_novamente = False


