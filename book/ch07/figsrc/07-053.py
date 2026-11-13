import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 8, 80, 22, 0.3, 0.6, step=0.1, arrow_right=False)
pts = [(1 / 3, r'$\frac{1}{3}$'), (0.4, r'$\frac{2}{5}$'), (0.5, r'$\frac{1}{2}$')]
for v, lab in pts:
    disc(ax, f(v), 22, 1.5, 'sujet'); text(ax, f(v), 34, lab, 'sujet', 'l')
for (a, _), (b, _) in zip(pts, pts[1:]):
    text(ax, (f(a) + f(b)) / 2, 34, '<', 'resultat', 16, weight='bold')
arrow(ax, (14, 6), (74, 6), 'varie')
text(ax, 14, 11, 'plus petit', 'fixe', 's', ha='left'); text(ax, 74, 11, 'plus grand', 'fixe', 's', ha='right')
save(fig, '07-053')
