import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
k = 4
def panel(ox, oy, a, b, la, lb, off_a, off_b, res, rr):
    arrow(ax, (ox, oy), (ox + a[0] * k, oy + a[1] * k), 'sujet', lw=1.3)
    arrow(ax, (ox, oy), (ox + b[0] * k, oy + b[1] * k), 'autre', lw=1.3)
    text(ax, ox + a[0] * k + off_a[0], oy + a[1] * k + off_a[1], la, 'sujet', 'm')
    text(ax, ox + b[0] * k + off_b[0], oy + b[1] * k + off_b[1], lb, 'autre', 'm')
    text(ax, ox + 14, 6, res, rr, 'm')
panel(6, 16, (3, 4), (5, 0), r'$x$', r'$y$', (-3, 1), (3.5, 0), r'$\langle x,y\rangle=15$', 'resultat')
panel(56, 16, (-1.4, 4.8), (3, 4), r'$Ax$', r'$Ay$', (-1, 4), (3.5, 1.5), r'$\langle Ax,Ay\rangle=15$', 'resultat')
text(ax, 20, 48, 'avant', 'encre', 's'); text(ax, 66, 48, 'après', 'encre', 's')
arrow(ax, (33, 28), (45, 28), 'varie'); text(ax, 39, 32, r'$A$', 'varie', 'm')
text(ax, 44, 6, '=', 'encre', 'l')
save(fig, '73-222')
