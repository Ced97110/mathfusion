import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, 'parcours fermé le plus long', 'varie', 'm')
text(ax, 44, 61, 'chaque forme a 8 éléments', 'sujet', 's')
# colonne de 8 cases : tout le parcours
for i in range(8):
    box(ax, 10, 26 + i * 3.75, 10, 3.75, 'varie', r=0.3, lw=0.6)
# grille 4 lignes x 2 colonnes : une colonne parcourue
for i in range(4):
    for j in range(2):
        box(ax, 35 + j * 8, 26 + i * 7.5, 8, 7.5, 'varie' if j == 0 else 'sujet', r=0.3, lw=0.6)
# cube : deux carrés reliés, 8 sommets
cxx, cyy, A, B = 70, 42, 12, 5.5
outer = [(-A, -A), (A, -A), (A, A), (-A, A)]
inner = [(-B, -B), (B, -B), (B, B), (-B, B)]
for i in range(4):
    j = (i + 1) % 4
    line(ax, [(cxx + outer[i][0], cyy + outer[i][1]), (cxx + outer[j][0], cyy + outer[j][1])], 'fixe')
    line(ax, [(cxx + inner[i][0], cyy + inner[i][1]), (cxx + inner[j][0], cyy + inner[j][1])], 'fixe')
    line(ax, [(cxx + outer[i][0], cyy + outer[i][1]), (cxx + inner[i][0], cyy + inner[i][1])], 'fixe')
arrow(ax, (cxx - A + 2, cyy - A), (cxx + A - 2, cyy - A), 'varie', lw=1.4, both=True)
for k, (x, y) in enumerate(outer + inner):
    disc(ax, cxx + x, cyy + y, 1.8, 'varie' if k < 2 else 'sujet')
text(ax, 15, 19, 'colonne', 'sujet', 's')
text(ax, 43, 19, 'grille 4 × 2', 'sujet', 's')
text(ax, 70, 19, 'cube', 'sujet', 's')
text(ax, 15, 11, 'longueur 8', 'varie', 'm')
text(ax, 43, 11, 'longueur 4', 'varie', 'm')
text(ax, 70, 11, 'longueur 2', 'varie', 'm')
save(fig, '60-103')
