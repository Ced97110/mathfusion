import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# gauche : ℤ, une seule droite
text(ax, 22, 66, 'ℤ', 'sujet', 'l', weight='bold')
for i in range(-3, 4):
    disc(ax, 22 + i * 5.2, 44, 1.5, 'sujet')
arrow(ax, (22, 49), (27.2, 49), 'varie', lw=1.4)
text(ax, 22, 54, 'base (1)', 'varie', 's')
text(ax, 22, 31, 'un seul morceau :', 'limite', 's')
text(ax, 22, 26.5, 'pas de découpe en 2', 'limite', 's')
# droite : ℤ², deux axes
cx, cy = 66, 44
for i in range(-2, 3):
    for j in range(-2, 3):
        r = 'sujet' if (j == 0) else ('autre' if i == 0 else 'fixe')
        disc(ax, cx + i * 6, cy + j * 6, 1.4, r)
text(ax, 66, 66, 'ℤ²', 'sujet', 'l', weight='bold')
text(ax, 66, 24, 'base (1, 0) et (0, 1)', 'varie', 's')
box(ax, 44, 12, 42, 8, 'resultat', label='axe bleu + axe violet', size='s')
text(ax, 22, 12, 'libre ≠ décomposable', 'encre', 's', weight='bold')
save(fig, '58-328')
