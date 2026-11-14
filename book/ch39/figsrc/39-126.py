import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
R = 14; Y = 40
lx, rx = 20, 68
def pL(k, r=R):
    a = math.radians(45 * k); return (lx + r * math.cos(a), Y + r * math.sin(a))
def pR(k, r=R):
    a = math.radians(90 - 45 * k); return (rx + r * math.cos(a), Y + r * math.sin(a))
ax.add_patch(Circle((lx, Y), R, ec=COL['fixe'], fc='none', lw=0.6, zorder=1, ls='--'))
ax.add_patch(Circle((rx, Y), R, ec=COL['fixe'], fc='none', lw=0.6, zorder=1, ls='--'))
for k in range(8):
    role = {5: 'sujet', 6: 'sujet', 3: 'resultat'}.get(k, 'fixe')
    x, y = pL(k); disc(ax, x, y, 1.6, role)
    role2 = {5: 'autre', 6: 'autre', 3: 'resultat'}.get(k, 'fixe')
    x, y = pR(k); disc(ax, x, y, 1.6, role2)
for k, r in [(5, 'sujet'), (6, 'sujet'), (3, 'resultat')]:
    x, y = pL(k, R + 4.5); text(ax, x, y, r'$\omega^%d$' % k, r, 's')
for k, r in [(5, 'autre'), (6, 'autre'), (3, 'resultat')]:
    x, y = pR(k, R + 3.5); text(ax, x, y, str(k), r, 's')
text(ax, lx, 64, 'racines de l’unité', 'sujet', 's')
text(ax, lx, 60, r'on multiplie', 'sujet', 's')
text(ax, rx, 64, 'heures', 'autre', 's')
text(ax, rx, 60, 'on additionne', 'autre', 's')
arrow(ax, (lx + 22, Y), (rx - 22, Y), 'resultat', lw=1.0, both=True)
text(ax, 44, Y + 4, r'$\omega^k \leftrightarrow k$', 'resultat', 's')
text(ax, lx, 12, r'$\omega^5\cdot\omega^6=\omega^3$', 'sujet')
text(ax, rx, 12, r'$5+6=3$', 'autre')
text(ax, 44, 4, 'même table : isomorphes', 'resultat', 's')
save(fig, '39-126')
