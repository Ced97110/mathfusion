import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 52, 4, 30, 60, 'sujet', fill=True)
text(ax, 67, 70, r'codomaine $T$', 'sujet', 'm', weight='bold'); text(ax, 14, 70, r'départ $S$', 'fixe', 'm')
Ty = lambda v: 10 + 9 * v
for v in range(6):
    got = v % 2 == 0
    disc(ax, 67, Ty(v), 3.3, 'resultat' if got else ('limite' if v == 3 else 'fixe'), label=str(v), size='s')
for s in range(3):
    disc(ax, 14, Ty(2 * s), 3.3, 'fixe', label=str(s), size='s')
    arrow(ax, (18, Ty(2 * s)), (62.5, Ty(2 * s)), 'resultat')
text(ax, 38, Ty(2) + 3.5, r'$\times2$', 'varie', 'm')
arrow(ax, (47, Ty(3)), (62.5, Ty(3)), 'limite'); text(ax, 28, Ty(3), 'jamais obtenu', 'limite', 's')
save(fig, '42-175')
