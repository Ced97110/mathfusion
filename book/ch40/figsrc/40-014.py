import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(64)
# gauche : grille ordinaire, 4 colonnes x 3 lignes de 8 mm
g0 = (4.0, 14.0); cell = 8.0
for i in range(5):
    line(ax, [(g0[0] + i * cell, g0[1]), (g0[0] + i * cell, g0[1] + 3 * cell)], 'fixe', lw=0.4)
for j in range(4):
    line(ax, [(g0[0], g0[1] + j * cell), (g0[0] + 4 * cell, g0[1] + j * cell)], 'fixe', lw=0.4)
line(ax, [(g0[0] + 3 * cell, g0[1]), (g0[0] + 3 * cell, g0[1] + 2 * cell)], 'sujet', lw=1.2)
line(ax, [(g0[0], g0[1] + 2 * cell), (g0[0] + 3 * cell, g0[1] + 2 * cell)], 'sujet', lw=1.2)
disc(ax, g0[0] + 3 * cell, g0[1] + 2 * cell, 1.2, 'resultat')
text(ax, g0[0] + 3 * cell, g0[1] - 3.5, 'colonne 3', 'sujet', 's')
text(ax, g0[0] + 12, g0[1] + 3 * cell + 4, 'ligne 2 : en haut', 'sujet', 's')
text(ax, 20, 59, 'grille ordinaire', 'encre', 's')
# droite : grille polaire
s = 9.0; c = (64.0, 30.0)
pp = lambda r, t: (c[0] + s * r * cos(t), c[1] + s * r * sin(t))
for r in (0.5, 1, 1.5, 2):
    ax.add_patch(Circle(c, s * r, ec=COL['sujet'] if r == 1.5 else COL['fixe'], fc='none', lw=1.2 if r == 1.5 else 0.4, zorder=1))
for k in range(12):
    t = radians(30 * k)
    line(ax, [c, pp(2, t)], 'sujet' if k == 2 else 'fixe', lw=1.2 if k == 2 else 0.3)
disc(ax, *pp(1.5, radians(60)), 1.2, 'resultat')
text(ax, 64, 59, 'grille polaire', 'encre', 's')
text(ax, 64, 5, 'cercle 1,5 et rayon 60°', 'sujet', 's')
save(fig, '40-014')
