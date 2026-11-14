import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def ring(cx, cy, n, sub, R=9):
    for k in range(n):
        x = cx + R * math.sin(2 * math.pi * k / n); y = cy + R * math.cos(2 * math.pi * k / n)
        disc(ax, x, y, 2.6, 'varie' if k in sub else 'sujet', label=str(k), size='s')
ring(22, 38, 4, [0, 2])
ring(66, 38, 3, [])
text(ax, 22, 60, 'facteur de 4 éléments', 'sujet', 's')
text(ax, 66, 60, 'facteur de 3 éléments', 'sujet', 's')
text(ax, 22, 22, r'sous-groupe $\{0,2\}$', 'varie', 's')
text(ax, 66, 22, 'aucun sous-groupe', 'fixe', 's')
text(ax, 22, 14, 'on peut insérer un terme', 'varie', 's', weight='bold')
text(ax, 66, 14, 'rien à insérer', 'resultat', 's', weight='bold')
text(ax, 44, 4, r'simple $\Leftrightarrow$ rien à insérer', 'encre', 's')
save(fig, '64-073')
