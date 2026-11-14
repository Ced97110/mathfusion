import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
# ligne 1 : colonne, + 1 avance d'une case
b = 68
for i in range(8):
    box(ax, 8, b + i * 3.6, 10, 3.6, 'sujet', r=0.3, lw=0.6)
arrow(ax, (24, b + 7.5 * 3.6), (24, b + 6.5 * 3.6), 'varie')
text(ax, 44, b + 14, 'colonne : + 1 avance\nd’une case', 'encre', 's', ha='left')
# ligne 2 : grille 4 x 2
g = 38
for i in range(4):
    for j in range(2):
        box(ax, 8 + j * 8, g + i * 7, 8, 7, 'sujet', r=0.3, lw=0.6)
arrow(ax, (30, g + 3.5 * 7), (30, g + 2.5 * 7), 'varie')
arrow(ax, (10, g - 3), (22, g - 3), 'autre')
text(ax, 44, g + 14, 'grille : (1, 0) descend\nd’une ligne ;\n(0, 1) va à droite', 'encre', 's', ha='left')
# ligne 3 : cube
o = (22, 4)
cubes(ax, [(0, 0, 0)], o, 12, 'sujet')
p0 = iso(0, 0, 0, o, 12)
for q, r in [((1, 0, 0), 'varie'), ((0, 1, 0), 'autre'), ((0, 0, 1), 'resultat')]:
    arrow(ax, p0, iso(*q, o, 12), r, lw=1.4)
text(ax, 44, 16, 'cube : (1, 0, 0), (0, 1, 0)\net (0, 0, 1) suivent\nune arête', 'encre', 's', ha='left')
save(fig, '60-105')
