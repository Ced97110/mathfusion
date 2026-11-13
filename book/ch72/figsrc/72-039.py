import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def ax2(ax, cx, cy, r):
    arrow(ax, (cx - r, cy), (cx + r, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - r), (cx, cy + r), 'fixe', lw=0.6)

ax2(ax, 22, 36, 17); ax2(ax, 66, 36, 17)
line(ax, [(6, 36), (38, 36)], 'sujet', lw=1.6)
line(ax, [(22, 20), (22, 52)], 'autre', lw=1.6)
disc(ax, 22, 36, 1.6, 'resultat')
line(ax, [(52, 22), (80, 50)], 'limite', lw=1.8)
text(ax, 34, 40, r'$U$', 'sujet', 'm'); text(ax, 26, 50, r'$U^\perp$', 'autre', 'm')
text(ax, 22, 58, 'non dégénéré', 'sujet', 'm')
text(ax, 22, 13, 'seul 0 en commun', 'resultat', 's')
text(ax, 66, 58, 'dégénéré', 'limite', 'm')
text(ax, 72, 54, r'$U = U^\perp$', 'limite', 's')
text(ax, 66, 13, 'toute la droite en commun', 'limite', 's')
save(fig, '72-039')
