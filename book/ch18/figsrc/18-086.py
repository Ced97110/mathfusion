import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
text(ax, 44, 92, r'$x^2-7x+12$', 'sujet', 'l')
labs = ['1  facteur commun', '2  signes', '3  couples', '4  écriture', '5  vérification']
res = ['rien à retirer', r'$-$ et $-$', r'$-3$ et $-4$', r'$(x-3)(x-4)$', r'$=x^2-7x+12$']
for i, (a, b) in enumerate(zip(labs, res)):
    y = 72 - i * 17
    box(ax, 4, y, 38, 10, 'sujet', label=a, size='s')
    arrow(ax, (42, y + 5), (47, y + 5), 'varie')
    box(ax, 47, y, 37, 10, 'resultat', label=b, size='s')
    if i < 4: arrow(ax, (23, y), (23, y - 7), 'fixe')
save(fig, '18-086')
