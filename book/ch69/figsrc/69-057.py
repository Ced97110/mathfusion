import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = numberline(ax, 8, 70, 10, -2, 3, arrow_right=True)
for v in (-1, 1):
    disc(ax, f(v), 10, 1.6, 'resultat')
text(ax, f(1) + 7, 16, 'racines', 'resultat', 's')
rows = [(30, True, r'$[-1,\,2]$', '2 racines', 'sujet'), (48, False, r'$(-1,\,2)$', '1 racine', 'autre')]
for y, closed, lab, nb, role in rows:
    line(ax, [(f(-1), y), (f(2), y)], role, lw=3.0)
    for v in (-1, 2):
        disc(ax, f(v), y, 2.0, role, fill=closed)
        line(ax, [(f(v), 12), (f(v), y - 2.2)], 'fixe', lw=0.4, dash=True)
    text(ax, f(-1) - 4, y, lab, role, 's', ha='right')
    text(ax, f(2) + 4, y, nb, role, 's', ha='left')
line(ax, [(f(1), 12), (f(1), 46)], 'resultat', lw=0.4, dash=True)
save(fig, '69-057')
