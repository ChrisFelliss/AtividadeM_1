# 10. Faça uma função que recebe a média final de um aluno por parâmetro e
# retorna o seu conceito, conforme a tabela abaixo:
# Nota Conceito
# de 0,0 a 4,9 D
# de 5,0 a 6,9 C
# de 7,0 a 8,9 B
# de 9,0 a 10,0A
#
# def funcao(num):
#     condicoes = {'D': 0 <= num < 5,
#                  'C': 5 <= num < 7,
#                  'B': 7 <= num < 9,
#                  'A': 9 <= num <= 10,
#                  Exception: 0 < num > 10 or type(num) == float}
#     print(condicoes.values())
#     for i in condicoes.values():
#         if i:
#             print(condicoes[i])
#             print(condicoes[i])
#             return condicoes[i]
# print(funcao(3))

def funcao(num):
    if type(num) == str or 0 < num > 10:
        return Exception
    if 0 <= num < 5:
        return 'D'
    if 5 <= num < 7:
        return 'C'
    if 7 <= num < 9:
         return 'B'
    if 9 <= num <= 10:
        return 'A'

print(funcao(3))


