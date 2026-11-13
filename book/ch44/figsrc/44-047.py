import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 46, 72, 'image de 1', 'fixe', 's'); text(ax, 70, 72, 'image de 2', 'fixe', 's')
rows = [(r'$1_S$', 1, 2), (r'$\alpha$', 2, 1), (r'$\beta$', 1, 1), (r'$\gamma$', 2, 2)]
for (n, a, b), y in zip(rows, [58, 42, 26, 10]):
    box(ax, 3, y - 6, 82, 12, 'fixe'); text(ax, 14, y, n, 'sujet', 'l', weight='bold')
    disc(ax, 46, y, 3.8, 'resultat', label=str(a)); disc(ax, 70, y, 3.8, 'resultat', label=str(b))
save(fig, '44-047')
