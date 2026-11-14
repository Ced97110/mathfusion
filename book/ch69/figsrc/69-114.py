import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
f = numberline(ax, 12, 72, 10, -2, 2, 1)
rows = [(44, -2, 1, 'sujet', r'$=2$', 'comptée', 1), (31, -1, 2, 'sujet', r'$=1$', 'non comptée', -1), (18, -2, 1.5, 'resultat', r'$=2$', 'bornes hors racines', 0)]
for r in (-1, 1):
    line(ax, [(f(r), 12), (f(r), 54)], 'fixe', dash=True, lw=0.7)
for y, a, b, role, res, flag, which in rows:
    line(ax, [(f(a), y), (f(b), y)], role, lw=2.0)
    disc(ax, f(a), y, 1.3, role)
    disc(ax, f(b), y, 1.3, role)
    text(ax, 80, y, res, role, 'm')
    if which == 1:
        text(ax, f(1) - 8, y + 4.5, flag, 'sujet', 's')
    elif which == -1:
        text(ax, f(-1) + 9, y + 4.5, flag, 'fixe', 's')
    else:
        text(ax, f(0), y + 4.5, flag, 'resultat', 's')
save(fig, '69-114')
