import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# product of two cyclic groups, orders 2 and 4 : 2 x 4 = 8 elements, lcm = 4, every element satisfies x^4 = 1
text(ax, 44, 61, r'ordres 2 et 4 : $m = 4$', 'sujet', 'm')
text(ax, 55, 52, 'ordre 4', 'sujet', 's')
text(ax, 8, 33, 'ordre 2', 'sujet', 's', rot=90)
for i in range(4):
    for j in range(2):
        disc(ax, 27 + i * 17, 31 - j * 14, 4.6, 'resultat')
brace(ax, 20, 86, 11, 'resultat', label=r'8 éléments : tous $x^4 = 1$', size='s')
save(fig, '67-082')
