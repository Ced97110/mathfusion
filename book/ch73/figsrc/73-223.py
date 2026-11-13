import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def panel(P, Q, la, lb, oa, ob, corner, role, lab, cx):
    line(ax, [P, corner, Q], 'fixe', dash=True)
    line(ax, [P, Q], role, lw=1.6)
    disc(ax, P[0], P[1], 1.3, role); disc(ax, Q[0], Q[1], 1.3, role)
    text(ax, P[0] + oa[0], P[1] + oa[1], la, role, 'm'); text(ax, Q[0] + ob[0], Q[1] + ob[1], lb, role, 'm')
    text(ax, cx, 6, lab, role, 'm')
k = 4
panel((20, 30), (28, 14), r'$x$', r'$y$', (-3, 1.5), (3, -1), (28, 30), 'sujet', r'$\|x-y\|^2=20$', 20)
panel((52.4, 33.2), (70, 30), r'$Ax$', r'$Ay$', (-1, 4), (3.5, -2), (70, 33.2), 'resultat', r'$\|Ax-Ay\|^2=20$', 64)
text(ax, 20, 46, 'avant', 'encre', 's'); text(ax, 62, 46, 'après', 'encre', 's')
arrow(ax, (34, 24), (46, 24), 'varie'); text(ax, 40, 27.5, r'$A$', 'varie', 'm')
text(ax, 42, 6, '=', 'encre', 'l')
save(fig, '73-223')
