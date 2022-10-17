# 5! = 5 * 4 * 3 * 2 * 1 (se multiplica 2 * 1)
# 5! = 5 * 4 * 3 * 2 (se multiplica 2 * 3)
# 5! = 5 * 4 * 6 (se multiplica 4 * 6)
# 5! = 5 * 24 (se multiplica 5 * 24 para finalizar la recursion)
# 5! = 120

def factorial(valor):
    valor = valor
    if valor == 1:
        return 1
    else:
        return valor * factorial(valor - 1)
resultado = factorial(5)
print(f'El factorial de 5 es: {resultado}')    
