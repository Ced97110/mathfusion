import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 62, r'$3\mid12$ donc $(12)\subseteq(3)$', 'resultat', 'm')
f = numberline(ax, 14, 80, 22, 0, 24, 3, every=4, arrow_right=False)
text(ax, 2, 50, '(12)', 'sujet', 'm', ha='left', weight='bold')
text(ax, 2, 34, '(3)', 'autre', 'm', ha='left', weight='bold')
for v in (0, 12, 24):
    line(ax, [(f(v), 48.5), (f(v), 35.5)], 'fixe', dash=True)
    disc(ax, f(v), 50, 1.8, 'sujet')
for v in range(0, 25, 3):
    disc(ax, f(v), 34, 1.8, 'limite' if v == 3 else 'autre', fill=(v != 3))
text(ax, f(3), 40, '$3$', 'limite', 's')
text(ax, 44, 7, '3 est dans (3), pas dans (12)', 'limite', 's')
save(fig, '56-085')
