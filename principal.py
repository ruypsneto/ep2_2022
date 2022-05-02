# aqui vamo importar as funções do arquivo 'funçoes' pra rodar o sistema
import funcoes as f 
from base_de_dados import dados
from base_de_dados import raio_terra

quer_jogar_novamente = True
jogo = True 
dados_convertidos = f.normaliza(dados)

while quer_jogar_novamente == True:         # aqui vai deixar o jogo em loop ate que o jogador nao queira mais 
    while jogo == True:        # aqui vai ser onde roda o jogo 
        # estrutura a pensar, tem um break pra n ferrar com o codigo mas depois tira 
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