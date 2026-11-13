import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

cx, cy, r = 44, 44, 26
fig, ax = canvas(88)
disc(ax, cx, cy, r, 'fixe', fill=False, lw=1.6)
text(ax, cx + 14, cy - 15, r'$\mathbb{T}$ : tout le cercle', 'fixe', 's')
poly(ax, [(cx + r * math.cos(math.radians(90 * k)), cy + r * math.sin(math.radians(90 * k))) for k in range(4)], 'sujet', fill=False, lw=0.6)
labs = ['1', r'$i$', '−1', r'$-i$']
offs = [(3, 3, 'left'), (3, 1.5, 'left'), (-3, 3, 'right'), (3, -1.5, 'left')]
for k in range(4):
    x, y = cx + r * math.cos(math.radians(90 * k)), cy + r * math.sin(math.radians(90 * k))
    disc(ax, x, y, 1.6, 'sujet')
    text(ax, x + offs[k][0], y + offs[k][1], labs[k], 'sujet', 'm', ha=offs[k][2])
text(ax, cx, cy + 3, 'les 4 racines :', 'sujet', 's')
text(ax, cx, cy - 3, 'un ensemble fini', 'sujet', 's')
text(ax, 4, 84, r'$u^4=1\ \Rightarrow\ |u|=1$', 'resultat', 's', ha='left')
text(ax, 84, 4, 'le produit reste dedans', 'resultat', 's', ha='right')
save(fig, '39-107')
