import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
y = 28
f = numberline(ax, 40, 80, y, 0, 2, step=0.25, every=4, arrow_right=False)
arrow(ax, (80, y), (85, y), 'fixe', lw=0.9)
line(ax, [(8, y), (40, y)], 'autre', lw=0.9)
for v in (-1,):
    xx = 40 + v * 20
    ax.plot([xx, xx], [y - 1.2, y + 1.2], color=COL['autre'], lw=0.8, zorder=1.5)
    text(ax, xx, y - 3.4, r'$-%d$' % -v, 'autre', 's')
arrow(ax, (40, y), (7, y), 'autre', lw=0.9)
text(ax, 22, 37, 'à gauche de 0 :', 'autre', 's')
text(ax, 22, 34, 'nombres négatifs', 'autre', 's')
for v, lab, r in ((0.75, r'$3/4$', 'sujet'), (1.25, r'$5/4$', 'resultat')):
    disc(ax, f(v), y, 1.3, r)
    text(ax, f(v), y + 4, lab, r, 'm')
text(ax, 62, 37, 'à droite de 0', 'fixe', 's')
brace(ax, f(0), f(0.75), 21, 'sujet', label='3 parts')
brace(ax, f(0), f(1.25), 11, 'resultat', label='5 parts')
save(fig, '06-088')
