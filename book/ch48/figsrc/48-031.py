import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 55, r'$G$ = entiers, en 4 paquets', 'sujet', 's')
contents = ['0  4  8 …', '1  5  9 …', '2  6  10 …', '3  7  11 …']
for i, c in enumerate(contents):
    x = 2.5 + i * 21.5
    box(ax, x, 26, 19, 20, 'sujet' if i == 0 else 'fixe', label=c, size='s')
    text(ax, x + 9.5, 21, f'paquet de {i}', 'sujet' if i == 0 else 'fixe', 's')
brace(ax, 2.5, 85.5, 16, 'resultat', label=r'$G/K$ : 4 éléments', depth=2.5)
save(fig, '48-031')
