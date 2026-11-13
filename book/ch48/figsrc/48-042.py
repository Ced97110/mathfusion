import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 57, 'bouton', 'resultat', 'm'); text(ax, 66, 57, 'double', 'limite', 'm')
line(ax, [(44, 8), (44, 52)], 'fixe', lw=0.5, dash=True)
for k in range(4):
    y = 44 - k * 11
    disc(ax, 34, y, 4.2, 'resultat', label=str(k), size='m')
    arrow(ax, (14, 30), (29, y + (30 - y) * 0.05), 'resultat', lw=0.8)
    hit = k % 2 == 0
    disc(ax, 80, y, 4.2, 'resultat' if hit else 'limite', fill=hit, label=str(k), size='m')
    if hit: arrow(ax, (58, 30), (75, y + (30 - y) * 0.05), 'limite' if False else 'resultat', lw=0.8)
text(ax, 8, 30, r'$\mathbb{Z}$', 'sujet', 'l'); text(ax, 52, 30, r'$\mathbb{Z}$', 'sujet', 'l')
text(ax, 22, 4, 'toutes atteintes', 'resultat', 's'); text(ax, 66, 4, '1 et 3 vides', 'limite', 's')
save(fig, '48-042')
