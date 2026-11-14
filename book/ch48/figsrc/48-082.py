import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 18, 64, 'Paquets', 'sujet', 'm', weight='bold')
text(ax, 70, 64, 'Positions', 'resultat', 'm', weight='bold')
pq = [r'$\{0,\ 4,\ 8\}$', r'$\{1,\ 5,\ 9\}$', r'$\{2,\ 6,\ 10\}$', r'$\{3,\ 7,\ 11\}$']
for i in range(4):
    y = 44 - i * 13
    box(ax, 2, y, 32, 9, 'sujet', label=pq[i], size='s')
    box(ax, 58, y, 24, 9, 'resultat', label=str(i), size='s')
    arrow(ax, (34.5, y + 4.5), (57.5, y + 4.5), 'varie')
text(ax, 46, 57, r'$\bar f$ : même nom', 'varie', 's')
text(ax, 46, 3, r'$\bar f$ ne change rien', 'varie', 's')
save(fig, '48-082')
