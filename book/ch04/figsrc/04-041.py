import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(92)

# radicande 16, sous le radical √
line(ax, [(8, 79), (10, 80.5), (13, 72), (16, 87), (34, 87)], 'fixe', lw=1.4)
text(ax, 25, 80, '16', 'sujet', 'l', weight='bold')
text(ax, 22, 66, 'radicande 16 : donné', 'sujet', 's')

# radicande 8, sous le radical ∛ (indice 3 agrandi)
line(ax, [(52, 79), (54, 80.5), (57, 72), (60, 87), (76, 87)], 'fixe', lw=1.4)
text(ax, 54.6, 84.2, '3', 'fixe', 'm', weight='bold')
text(ax, 68, 80, '8', 'sujet', 'l', weight='bold')
text(ax, 66, 66, 'radicande 8 : donné', 'sujet', 's')

# 16 est une aire : grille de 4 sur 4 carreaux (le total, en bleu)
for i in range(4):
    for j in range(4):
        box(ax, 12 + i * 5, 36 + j * 5, 4.6, 4.6, 'sujet', r=0.4)
text(ax, 22, 25.5, '16 carreaux : le total', 'sujet', 's')
# le côté, cherché, en orange
line(ax, [(12, 34), (31.6, 34)], 'varie', lw=1.4)
text(ax, 21.8, 31, 'côté ? cherché', 'varie', 's')

# 8 est un volume : cube de 2 × 2 × 2 (le total, en bleu)
cells = [(i, j, k) for i in range(2) for j in range(2) for k in range(2)]
cubes(ax, cells, (66, 34), 7, 'sujet')
text(ax, 66, 25.5, '8 cubes : le total', 'sujet', 's')
line(ax, [iso(0,0,0,(66,34),7), iso(2,0,0,(66,34),7)], 'varie', lw=1.4)
text(ax, 66, 30, 'côté ? cherché', 'varie', 's')

text(ax, 22, 15, 'bleu : donné au départ', 'sujet', 's')
text(ax, 66, 15, 'orange : à trouver', 'varie', 's')

save(fig, '04-041')
