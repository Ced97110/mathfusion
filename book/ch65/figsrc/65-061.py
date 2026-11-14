import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
text(ax, 44, 66, r'$x^3-x=x\,(x-1)(x+1)$', 'sujet', 'm', weight='bold')
facs = [('x', '0', 'sujet'), ('x−1', '1', 'autre'), ('x+1', '−1', 'autre')]
xs = [16, 44, 72]
for x, (fa, r, role) in zip(xs, facs):
    box(ax, x - 12, 44, 24, 11, role, label='facteur ' + fa if False else fa, size='s')
    arrow(ax, (x, 43.5), (x, 36.5), 'fixe', lw=0.8)
    disc(ax, x, 31, 4.2, role, label=r, size='m')
text(ax, 16, 53 + 6, 'facteur f₁', 'sujet', 's')
text(ax, 16, 21, 'seule racine de f₁', 'sujet', 's')
# forbidden move 0 -> 1
arrow(ax, (20.5, 36), (39.5, 36), 'limite', lw=1.2, curve=-0.5)
text(ax, 30, 45.5, '', 'limite', 's')
text(ax, 30, 12, '0 → 1 : impossible', 'limite', 'm', weight='bold')
text(ax, 58, 21, 'racines des autres facteurs', 'autre', 's')
text(ax, 44, 4.5, 'les racines de f₁ restent entre elles', 'resultat', 's')
save(fig, '65-061')
