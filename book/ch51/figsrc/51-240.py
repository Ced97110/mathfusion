import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X0, DX = 24.0, 10.5
ax_ = lambda k: X0 + (k - 1) * DX
YT, YB = 48.0, 14.0
text(ax, 2, YT, 'départs', 'sujet', 'm', ha='left')
text(ax, 2, YB, 'arrivées', 'resultat', 'm', ha='left')
text(ax, 2, 58, r'$x \mapsto 2x$ dans ℤ', 'encre', 'm', ha='left')
for k in (1, 2, 3):
    disc(ax, ax_(k), YT, 3.4, 'sujet', label=str(k))
for k in range(1, 7):
    if k == 1: role = 'limite'
    elif k % 2 == 0: role = 'resultat'
    else: role = 'fixe'
    disc(ax, ax_(k), YB, 3.4, role, label=str(k))
for k in (1, 2, 3):
    arrow(ax, (ax_(k), YT - 3.4), (ax_(2 * k), YB + 3.4), 'varie')
text(ax, ax_(1), 4.5, '1 : jamais atteint', 'limite', 'm', ha='left')
save(fig, '51-240')
