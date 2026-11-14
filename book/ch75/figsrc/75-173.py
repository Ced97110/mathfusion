import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, r'$U(2)$ : on conjugue la coordonnée 1', 'varie', 's', weight='bold')
for k, (x0, lab, r, tip, h) in enumerate([(4, 'avant', 'resultat', '$i$', '$H=-i$'), (48, 'après', 'limite', '$-i$', '$H=i$')]):
    ox, oy, u = x0 + 18, 42, 13
    box(ax, x0, 24, 36, 38, 'fixe', fill=True)
    text(ax, x0+18, 58, lab, 'fixe', 's', weight='bold')
    arrow(ax, (ox, oy), (ox+u, oy), 'sujet', lw=1.3)
    sgn = 1 if k == 0 else -1
    arrow(ax, (ox, oy), (ox, oy+sgn*u), r, lw=1.3)
    text(ax, ox+u+3, oy-3, '1', 'sujet', 's')
    text(ax, ox-4, oy+sgn*u, tip, r, 's')
    text(ax, x0+18, 18, h, r, 'm', weight='bold')
arrow(ax, (41, 43), (47, 43), 'varie')
text(ax, 22, 8, 'distances gardées', 'resultat', 's'); text(ax, 66, 8, '$H$ change : hors de $U(2)$', 'limite', 's')
save(fig, '75-173')
