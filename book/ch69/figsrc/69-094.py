import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
f = numberline(ax, 10, 70, 14, -2, 2, 1)
rows = [(r'$f_0$', 'sujet', [-1.88, 0.35, 1.53], 46), (r'$f_1$', 'autre', [-1, 1], 36), (r'$f_2$', 'varie', [0.5], 26)]
for lab, role, roots, y in rows:
    text(ax, 4.5, y, lab, role, 'm')
    line(ax, [(10, y), (f(2), y)], 'fixe', lw=0.5)
    for r in roots:
        line(ax, [(f(r), y - 1.5), (f(r), 14.6)], 'fixe', dash=True, lw=0.5)
        disc(ax, f(r), y, 1.5, role)
        disc(ax, f(r), 14, 1.0, 'varie')
text(ax, 44, 55, 'signe qui change = racine', 'encre', 'm')
text(ax, 44, 3.5, r'$V$ peut changer en ces 6 points', 'varie', 'm')
save(fig, '69-094')
