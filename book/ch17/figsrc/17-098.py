import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(66)
f = numberline(ax, 12, 62, 12, -3, 2, labels=False)
seg(ax, f, -2, 1, 12, 'sujet'); odot(ax, f(-2), 12, 'sujet', False); odot(ax, f(1), 12, 'sujet')
yA, yB = 49, 31
for (v, s, y, r) in [(-2, '$-2$', yB, 'sujet'), (0, '$x$', yB, 'varie'), (1, '$1$', yB, 'sujet')]:
    text(ax, f(v), y, s, r, 'l')
text(ax, (f(-2) + f(0)) / 2, yB, '$<$', 'fixe', 'l'); text(ax, (f(0) + f(1)) / 2, yB, r'$\leq$', 'fixe', 'l')
for (v, s, r) in [(1, '$1$', 'sujet'), (0, '$x$', 'varie'), (-2, '$-2$', 'sujet')]:
    text(ax, f(v), yA, s, r, 'l')
text(ax, (f(-2) + f(0)) / 2, yA, '$>$', 'fixe', 'l'); text(ax, (f(0) + f(1)) / 2, yA, r'$\geq$', 'fixe', 'l')
arrow(ax, (f(1) + 2, yA + 6), (f(-2) - 2, yA + 6), 'limite', curve=0.0)
text(ax, f(-0.5), yA + 10, 'on lit à contre-sens', 'limite', 's')
arrow(ax, (f(-2) - 2, yB - 6), (f(1) + 2, yB - 6), 'resultat')
text(ax, f(-0.5), yB - 10, 'on lit comme la droite', 'resultat', 's')
line(ax, [(f(-2), yB - 13), (f(-2), 15)], 'fixe', lw=0.5, dash=True); line(ax, [(f(1), yB - 13), (f(1), 15)], 'fixe', lw=0.5, dash=True)
save(fig, '17-098')
