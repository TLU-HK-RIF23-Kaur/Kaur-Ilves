import math

'''
Näidis ÜLESANNE
'''

def example_task():
    kaatet1 = int(input("Sisesta kolmnurga esimese kaateti pikkus ja vajuta enter: "))
    kaatet2 = int(input("Sisesta kolmnurga teise kaateti pikkus ja vajuta enter: "))
    pindala = kaatet1 * kaatet2 / 2
    hypotenuus = math.sqrt(kaatet1 ** 2 + kaatet2 ** 2)
    ymbermoot = math.fsum([kaatet1, kaatet2, hypotenuus])
    print("Kolmnurga pindala on", pindala, "ja ümbermõõt on ", ymbermoot)

