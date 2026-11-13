import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 3.0
def dots(ax, x, labs, ys, role):
    for l, y in zip(labs, ys): disc(ax, x, y, R, role, label=l)
def link(ax, pa, pb, role, dy=0.0, curve=0.0):
    s = 1 if pb[0] > pa[0] else -1
    arrow(ax, (pa[0] + s * R, pa[1] + dy), (pb[0] - s * R, pb[1] + dy), role, curve=curve)
fig, ax = canvas(74)
xs = (14, 44, 74); ys = [54, 40, 26]
for x, t in zip(xs, ('$A$', '$B$', '$C$')): text(ax, x, 68, t, 'sujet', 'l')
for x, L, role in zip(xs, (['1', '2', '3'], [r'$a$', r'$b$', r'$c$'], [r'$x$', r'$y$', r'$z$']), ('sujet', 'sujet', 'sujet')): dots(ax, x, L, ys, role)
for y in ys: link(ax, (xs[0], y), (xs[1], y), 'sujet'); link(ax, (xs[1], y), (xs[2], y), 'sujet')
text(ax, 29, 62, '$f$ : bijection', 'sujet', 's'); text(ax, 59, 62, '$g$ : bijection', 'sujet', 's')
arrow(ax, (14, 20), (74, 20), 'resultat', curve=0.0)
text(ax, 44, 14.5, '$g \\circ f$ : bijection', 'resultat', 'm')
text(ax, 44, 6, 'chaque point reçu une fois', 'resultat', 'm')
save(fig, '42-227')
