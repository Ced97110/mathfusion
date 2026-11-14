import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 4, 62, 80, 8, 'varie', label='1. tangente : calculatrice −71,57°', size='s')
cells = [(5, 34, 'resultat', r'$a<0,\ b>0$'), (45, 34, 'fixe', r'$a>0,\ b>0$'),
         (5, 8, 'fixe', r'$a<0,\ b<0$'), (45, 8, 'fixe', r'$a>0,\ b<0$')]
for x, y, role, lab in cells:
    box(ax, x, y, 38, 24, role)
    text(ax, x + 19, y + 17, lab, 'resultat' if role == 'resultat' else 'fixe', 's')
text(ax, 24, 47, 'A(−1 ; 3)', 'sujet', 's'); text(ax, 24, 40, '2. 108,43°', 'resultat', 'm', weight='bold')
arrow(ax, (44, 62), (24, 58), 'varie', curve=0.0)
save(fig, '35-041')
