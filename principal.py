#  aqui roda o jogo 
import funcoes as f 
from base_de_dados import dados
from base_de_dados import raio_terra
import termcolor 

 
logo ='                       /////////////////////////////////\n                               INSPER PELO MUNDO\n                       /////////////////////////////////\n \n \n  \n \n \n '
print(logo)

inicia_jogo = str(input('Iniciar Jogo[sim/nao]:'))

while inicia_jogo != 'sim':
    print(logo)
    inicia_jogo = str(input('Iniciar Jogo:'))


print('\n \n Tente adivinhar qual é o pais ')




quer_jogar_novamente = True
jogo = True 
dados_convertidos = f.normaliza(dados)      # dados que vamos utilizar 
while quer_jogar_novamente == True:         # aqui vai deixar o jogo em loop ate que o jogador nao queira mais 
    tentativas = 20 
    pais_sorteado = f.sorteia_pais(dados_convertidos)
    lat_pais = dados_convertidos[pais_sorteado]['geo']['latitude']
    long_pais = dados_convertidos[pais_sorteado]['geo']['longitude']
    lista_registro_tentativas = []
    lista_registro_dicas = []

    while jogo == True:        # aqui vai ser onde roda o jogo 


        if tentativas >= 15:
            cor_tentativas = 'blue'
        elif tentativas >= 8 :
            cor_tentativas = 'yellow'
        elif tentativas < 8:
            cor_tentativas = 'red'

        print('\n \n Voce tem', termcolor.colored(tentativas, cor_tentativas),'restantes')
        comandos = ' \n \n Digite \n dicas : vai para o mercado de dicas (gasta tentativas para a utilizacao delas) \n desisto : encerra a partida \n registro: aparece todas as dicas usadas \n \n \n '
        print(comandos)
        palpite = str(input('Qual seu palpite?')).lower()
        palpite = palpite.strip()
        


        if palpite == 'dicas':
            intedicas = '\n \n Bem vindo ao mercado de dicas \n////////////////////////////////////////////////////////\n// [1] Qual a area do pais ? -4 tentaivas            //\n// [2] Qual a população desse pais ?  -4 tentaivas  //\n// [3] Qual uma letra da capital ? -2 tentaivas    //\n// [4] Qual o continente desse pais ?-7 tentaivas //\n// [5] Qual as cores da bandeira? -5 tentaivas   //\n// [0] nenhuma dica                             //\n/////////////////////////////////////////////////'
            print(intedicas)

            n_dica = str(input('\n Qual dica deseja?[0/1/2/3/4/5]   '))

            if n_dica == '1':
               a = dados_convertidos[pais_sorteado]['area']
               ra = '{0} km²'.format(a)
               print('{0} km²'.format(a))
               lista_registro_dicas.append(ra)
               tentativas -= 4

            elif n_dica =='2':

                p = dados_convertidos[pais_sorteado]['populacao']
                print('{0} habitantes'.format(p))
                pop = '{0} habitantes'.format(p)
                lista_registro_dicas.append(pop)
                tentativas -= 4

            elif n_dica == '3':

                c = dados_convertidos[pais_sorteado]['capital']
                letras_capital = []
                l_c =  f.sorteia_letra(c, letras_capital)
                rletracapital = 'letra da capital é {}'.format(l_c)
                print(rletracapital)
                letras_capital.append(l_c)
                lista_registro_dicas.append(rletracapital)
                tentativas-= 2

            elif n_dica == '4':

                cont = dados_convertidos[pais_sorteado]['continente']
                rdica_continente = 'o continente é {}'.format(cont)
                print(rdica_continente)
                lista_registro_dicas.append(rdica_continente)
                tentativas -= 7

            elif n_dica == '5':

                b = dados_convertidos[pais_sorteado]['bandeira']
                for cor_ban, qtd in b.items():
                    if qtd > 0:
                        print(cor_ban)
                    lista_registro_dicas.append(cor_ban)
                tentativas -= 5

            elif n_dica == '0':
                palpite = str(input('Qual seu palpite?'))

            else:
                print('invalido')
                palpite = str(input('Qual seu palpite?'))

                

        elif palpite == 'desisto':
            print('Voce esta nervoso? \n Perdeu por desistencia')
            break

        elif palpite  == 'registro':
            for dica in lista_registro_dicas:
                print(dica)
        
        if tentativas <= 0:
            print('voce perdeu, nao te restam tentativas')
            break

        if palpite == pais_sorteado:
            
            print('Parabens voce venceu!!!!\n  \n  \n   ')
            print('Voce conseguio em {0}'.format(tentativas))
            break



        if palpite != 'dicas' and palpite != 'desisto' and palpite in dados_convertidos.keys() and palpite != 'registro':
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

                    elif registro[1] <= 4000:
                        cor = 'magenta'
                    
                    elif  registro[1] <= 6000:
                        cor= 'cyan'

                    elif registro[1] <= 8000:
                        cor = 'yellow'

                    else:
                        cor = 'white'
                    
                    info_a_printar = '{1} ------ {0:.1f} Km'.format(registro[1], registro[0])
                    print(termcolor.colored(info_a_printar, cor))



                
                tentativas -= 1
        
        elif palpite != 'dicas' and palpite != 'desisto':
            print('invalido')
    


    quer_jogar = str(input('Quer jogar novamente?[sim/nao]  '))
    while quer_jogar != 'sim' and quer_jogar != 'nao':
        print('invalido') 
        quer_jogar = str(input('Quer jogar novamente?[sim/nao]  '))
    if quer_jogar == 'sim':
            jogo == True 
    else:
        print('Obrigado por jogar!!!')
        quer_jogar_novamente = False
