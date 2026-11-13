import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$p(x)=x^3+x^2+2$ dans $\mathbb{Z}/3$', 'sujet', 'm')
rows = [(0, '0 + 0 + 2 = 2', '2'),
        (1, r'$1+1+2=4\equiv 1$', '1'),
        (2, r'$8+4+2=14\equiv 2$', '2')]
y = 46
for a, calc, val in rows:
    box(ax, 2, y, 16, 10, 'varie', label=f'x = {a}', size='m')
    arrow(ax, (18.5, y + 5), (23, y + 5), 'fixe')
    box(ax, 23, y, 40, 10, 'fixe', label=calc, size='m')
    arrow(ax, (63.5, y + 5), (68, y + 5), 'fixe')
    box(ax, 68, y, 18, 10, 'sujet', label=f'p = {val}', size='m')
    y -= 14
text(ax, 44, 8, 'aucune valeur nulle : pas de racine', 'resultat', 'm', weight='bold')
save(fig, '54-208')
