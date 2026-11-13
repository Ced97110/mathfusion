import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *

fig, ax = canvas(66)

# Colonne de gauche : les trois estimations, dans l'ordre
text(ax, 9, 61, 'estimation', 'varie', 's')
for y, estimation in ((52, '600'), (42, '10'), (32, '8')):
    box(ax, 3, y - 3.5, 12, 7, 'varie', label=estimation, size='m')

# Colonne du milieu : chaque soustraction et le reste qu'elle laisse
text(ax, 38.5, 52, r'4 944 − 600 $\times$ 8 = 144', 'encre', 'm')
text(ax, 38.5, 42, r'144 − 10 $\times$ 8 = 64', 'encre', 'm')
text(ax, 38.5, 32, r'64 − 8 $\times$ 8 = 0', 'encre', 'm')

# Colonne de droite : aucune estimation corrigée
text(ax, 73, 61, 'estimation corrigée', 'limite', 's')
for y in (52, 42, 32):
    box(ax, 62, y - 3.5, 22, 7, 'limite', fill=False, dash=True, label='aucune', size='s')

# Bilan sous le trait
line(ax, [(3, 25), (86, 25)], 'fixe', lw=0.9)
text(ax, 24, 18, '600 + 10 + 8 = 618', 'resultat', 'm')
box(ax, 61, 13, 24, 10, 'resultat', label='reste final : 0', size='s')

save(fig, '03-065')
