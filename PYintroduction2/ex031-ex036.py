#crie uma funcao voto, receba como parametro o ano de nasc, retornando um valor literal mostrando se uma pessoa tem voto negado
#opcional ou obrigatorio
"""
def voto(year = 0):
    from datetime import date
    n = date.today().year - year
    if n < 16:
        print('no vote')
    elif n >= 18 and n <= 70:
        print('need to vote')
        print(n)
    else:
        print('optional vote')
voto(1940)
"""
#funcao fatorial, receba 2 parametros, o primeiro que indique o n a calcular e o outro chamado show, valor logico opcional
#indicando se sera mostrado ou nao na tela o processo de calculo do fatorial
def factorial(n , show = False):
    num = 0
    for i in range(5, 0):
        num = n * (n-1)
    print(num)
factorial(5, show = True)



#funcao ficha, 2 parametros, nome e qtd de gols, mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado
#corretamente

#funcao leiaint, funcionar como o input, mas fazer validacao para aceitar apenas um valor numerico

#funcao notas, receber n notas, retornar um dicionario com as informacoes: qtd de notas, maior nota, media, situacao(aprv ou rprv)
#adicionar docstring

#mini sitema que utilize o interactive help, usuario vai digitar o comando e o manual vai aparecer, quando o usuario
#digitar a palavra 'fim', o programa se encerrara, use cores