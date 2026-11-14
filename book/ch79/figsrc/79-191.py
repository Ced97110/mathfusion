import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 4, 66, 80, 14, 'sujet', label=r'$d(a\vee b)+d(a\wedge b)=d(a)+d(b)$')
rows = [('diviseurs', 'rang : facteurs', r'$4+2=3+3$'), ('sous-espaces', 'rang : dimension', r'$3+1=2+2$'), ('parties', 'rang : éléments', r'$4+2=3+3$')]
for i, (n, rk, eq) in enumerate(rows):
    y = 44 - 20 * i
    arrow(ax, (44, 66 if i == 0 else 66), (14 + 0 * i, y + 14), 'fixe', lw=0.6) if False else None
    box(ax, 4, y, 30, 14, 'fixe', label=n)
    text(ax, 64, y + 10, eq, 'resultat', 'm', weight='bold'); text(ax, 64, y + 3, rk, 'fixe', 's')
save(fig, '79-191')
