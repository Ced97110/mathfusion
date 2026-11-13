import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
# --- gauche : z^4 = 1 ---
cx, cy, r = 22, 40, 14
text(ax, cx, 70, r'$z^4=1$', 'encre', 'l')
disc(ax, cx, cy, r, 'fixe', fill=False, lw=0.7)
roles = {0: 'sujet', 1: 'varie', 2: 'varie', 3: 'resultat'}
labs = {0: '1', 1: r'$i$', 2: '−1', 3: r'$-i$'}
offs = {0: (3, 3, 'left'), 1: (3, 2, 'left'), 2: (-3, 3, 'right'), 3: (3, -2, 'left')}
for k in range(4):
    x, y = cx + r * math.cos(math.radians(90 * k)), cy + r * math.sin(math.radians(90 * k))
    disc(ax, x, y, 1.4, roles[k])
    text(ax, x + offs[k][0], y + offs[k][1], labs[k], roles[k], 'm', ha=offs[k][2])
text(ax, cx, 14, r'$i\times(-1)=-i$', 'encre', 's')
text(ax, cx, 7, 'reste dans l’ensemble', 'resultat', 's')
# séparation
line(ax, [(44, 4), (44, 72)], 'fixe', lw=0.5, dash=True)
# --- droite : z^2 = 2 ---
text(ax, 66, 70, r'$z^2=2$', 'encre', 'l')
x0, x1, y0 = 47, 85, 40
line(ax, [(x0, y0), (x1, y0)], 'fixe', lw=0.7)
f = lambda v: 66 + v * 9.5
s2 = math.sqrt(2)
disc(ax, f(s2), y0, 1.4, 'sujet'); disc(ax, f(-s2), y0, 1.4, 'sujet'); disc(ax, f(2), y0, 1.4, 'limite')
text(ax, f(-s2), y0 + 4, r'$-\sqrt{2}$', 'sujet', 's')
text(ax, f(s2) - 2.5, y0 + 4, r'$\sqrt{2}$', 'sujet', 's')
text(ax, f(2) + 1, y0 - 4, '2', 'limite', 'm')
arrow(ax, (f(s2) + 1.5, y0 - 2), (f(2) - 1.5, y0 - 2), 'varie', lw=0.9, curve=0.5)
text(ax, 66, 24, r'$\sqrt{2}\times\sqrt{2}=2$', 'varie', 's')
text(ax, 66, 17, r'$2^2=4\neq 2$', 'limite', 's')
text(ax, 66, 7, 'sort de l’ensemble', 'limite', 's')
save(fig, '39-103')
