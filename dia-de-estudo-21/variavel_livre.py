# Variáveis livres + nonlocal (locals, globals)
print(globals())
def fora(x):
    a = x

    def dentro(): 

        return a # Variavel livre
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)



def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)