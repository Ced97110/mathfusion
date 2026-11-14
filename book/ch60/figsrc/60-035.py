import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 7, 69, 24, -5, 5, step=1)
for v in range(-5, 6):
    r = 'sujet' if v == 0 else ('autre' if v == 5 else 'fixe')
    disc(ax, f(v), 24, 1.9, r)
text(ax, f(0), 42, '0 : seul élément de torsion', 'sujet', 'm')
arrow(ax, (f(0), 39), (f(0), 27), 'sujet')
text(ax, 44, 8, 'a × 5 ≠ 0 dès que a ≠ 0', 'autre', 'm')
save(fig, '60-035')
