import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 3.0
def dots(ax, x, labs, ys, role):
    for l, y in zip(labs, ys): disc(ax, x, y, R, role, label=l)
def link(ax, pa, pb, role, dy=0.0, curve=0.0):
    s = 1 if pb[0] > pa[0] else -1
    arrow(ax, (pa[0] + s * R, pa[1] + dy), (pb[0] - s * R, pb[1] + dy), role, curve=curve)
fig, ax = canvas(80)
xs = (14, 44, 74); Y = {'A': [58, 42, 26], 'B': [50, 34], 'C': [58, 42, 26]}
for x, t in zip(xs, ('$A$', '$B$', '$C$')): text(ax, x, 72, t, 'sujet', 'l')
dots(ax, xs[0], ['1', '2', ''], Y['A'], 'fixe')
dots(ax, xs[1], [r'$a$', ''], Y['B'], 'fixe')
dots(ax, xs[2], ['', r'$y$', r'$z$'], Y['C'], 'fixe')
for i, j in ((0, 0), (1, 0)): link(ax, (xs[0], Y['A'][i]), (xs[1], Y['B'][j]), 'fixe')
link(ax, (xs[1], Y['B'][0]), (xs[2], Y['C'][2]), 'fixe')
disc(ax, xs[0], 26, R, 'resultat', label='3'); disc(ax, xs[1], 34, R, 'resultat', label=r'$b$'); disc(ax, xs[2], 58, R, 'varie', label=r'$x$')
link(ax, (xs[0], 26), (xs[1], 34), 'resultat'); link(ax, (xs[1], 34), (xs[2], 58), 'resultat')
text(ax, 29, 24, '$f$', 'resultat', 's'); text(ax, 52, 48, '$g$', 'resultat', 's')
text(ax, 74, 66, 'point choisi', 'varie', 's')
text(ax, 44, 12, 'on remonte de $C$ vers $A$', 'resultat', 'm')
save(fig, '42-226')
