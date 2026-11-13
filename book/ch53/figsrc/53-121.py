import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
# cas concret : 999 a 3 chiffres décimaux et 10 bits
text(ax, 44, 61, r'$512\leq 999\leq 1\,023$', 'fixe', 's')
for i in range(3):
    box(ax, 2 + i * 8, 44, 7, 10, 'sujet', label='9')
text(ax, 13, 39, '3 chiffres', 'sujet', 's')
arrow(ax, (27, 49), (34, 49), 'varie')
for i in range(10):
    box(ax, 36 + i * 5, 44, 4.6, 10, 'varie')
text(ax, 61, 39, '10 bits', 'varie', 's')
text(ax, 44, 30, 'plus de 3 bits par chiffre', 'fixe', 's')
# même rapport pour 300 chiffres
box(ax, 2, 6, 22, 14, 'sujet', label='300\nchiffres')
arrow(ax, (25, 13), (30, 13), 'varie')
box(ax, 31, 6, 24, 14, 'varie', label='≈ 1 000\nbits')
arrow(ax, (56, 13), (61, 13), 'varie')
box(ax, 62, 6, 24, 14, 'resultat', label='< 2 000\nmultiplications', size='s')
save(fig, '53-121')
