import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
X = lambda v: 44 + v * 11          # top: integers
Y = lambda v: 44 + v * 11 / 3      # bottom: same abscissa for 3v
line(ax, [(8, 62), (80, 62)], 'fixe'); line(ax, [(8, 26), (80, 26)], 'fixe')
for v in range(-9, 10):
    ax.plot([Y(v)] * 2, [25.2, 26.8], color=COL['fixe'], lw=0.5)
for v in range(-3, 4):
    disc(ax, X(v), 62, 1.6, 'sujet'); disc(ax, Y(3 * v), 26, 1.6, 'resultat')
    arrow(ax, (X(v), 59.8), (X(v), 28.4), 'varie' if v else 'resultat', lw=0.8)
for v in (0, 1, 2):
    text(ax, X(v), 67, str(v), 'sujet', 's'); text(ax, Y(3 * v), 20.5, str(3 * v), 'resultat', 's')
text(ax, 4, 74, r'$G$ = ℤ', 'sujet', 'm', ha='left')
text(ax, 4, 12, 'image = 3ℤ', 'resultat', 'm', ha='left')
text(ax, 84, 74, '×3 : un pour un', 'varie', 's', ha='right')
text(ax, 84, 12, 'noyau = {0}', 'resultat', 'm', ha='right')
save(fig, '48-179')
