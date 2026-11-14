import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 68, 'neuf éléments : 3 × 3', 'sujet')
labels = {(0, 0): '0', (1, 0): '1', (2, 0): '2',
          (0, 1): r'$i$', (1, 1): r'$1+i$', (2, 1): r'$2+i$',
          (0, 2): r'$2i$', (1, 2): r'$1+2i$', (2, 2): r'$2+2i$'}
for (a, b), s in labels.items():
    role = 'sujet'
    if (a, b) == (2, 1): role = 'varie'
    if (a, b) == (0, 1): role = 'resultat'
    box(ax, 18 + a * 17.5, 20 + b * 14, 16, 11, role, label=s)
text(ax, 9, 36, r'$b\in\{0,1,2\}$', 'fixe', rot=90)
brace(ax, 18, 69, 19, 'fixe', label=r'$a\in\{0,1,2\}$')
text(ax, 44, 7, r'$(2+i)^2=4+4i+2=i$', 'resultat')
save(fig, '67-162')
