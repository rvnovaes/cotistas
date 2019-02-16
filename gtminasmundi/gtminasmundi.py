import random
import numpy as np
from itertools import cycle, islice, chain


class Aluno:
    def __init__(self, tipo, nota):
        self.tipo = tipo
        self.nota = nota

    def __str__(self):
        return '''{tipo} - {nota}'''.format(tipo=self.tipo, nota=self.nota)


def gerar_grupo(tipo, n_alunos, min=60, max=100):
    notas = np.random.randint(min, max, n_alunos)
    notas = np.sort(notas)[::-1]
    grupo_alunos = list()
    for nota in notas:
        grupo_alunos.append(Aluno(tipo, nota))
    return grupo_alunos


def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))


separador = '==============='
c1 = gerar_grupo('c1', 10)
c2 = gerar_grupo('c2', 10)
c3 = gerar_grupo('c3', 10)
c4 = gerar_grupo('c4', 10)
ca = gerar_grupo('ca', 50)

print(*c1, sep='\t')
print(separador)
print(*c2, sep='\t')
print(separador)
print(*c3, sep='\t')
print(separador)
print(*c4, sep='\t')
print(separador)
print(*ca, sep='\t')
print(separador)

cotistas = roundrobin(c1, c2, c3, c4)
classificacao = roundrobin(cotistas, ca)

print('Proposta do GT')
print(*classificacao, sep='\t')

cotistas = c1 + c2 + c3 + c4
cotistas.sort(key=lambda x: x.nota, reverse=True)
classificacao = roundrobin(cotistas, ca)

print('Proposta Nova')
print(*classificacao, sep='\t')













