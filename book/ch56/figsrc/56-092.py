import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
f = lambda v: 46 + v * 3.6
y3, ym3, y6 = 58, 42, 20
text(ax, 44, 77, r'$3 \sim -3 \Leftrightarrow (3) = (-3)$', 'encre', 'm')
text(ax, 2, y3, '(3)', 'sujet', 's', ha='left')
text(ax, 2, ym3, '(−3)', 'autre', 's', ha='left')
text(ax, 2, y6, '(6)', 'fixe', 's', ha='left')
for v in range(-9, 10, 3):
    text(ax, f(v), y3 + 4.5, str(v).replace('-', '−'), 'sujet', 's')
    disc(ax, f(v), y3, 1.0, 'sujet')
    disc(ax, f(v), ym3, 1.0, 'autre')
    line(ax, [(f(v), ym3 + 1.2), (f(v), y3 - 1.2)], 'resultat', lw=0.8)
for v in (-6, 0, 6):
    disc(ax, f(v), y6, 1.0, 'fixe')
for v in (-3, 3):
    disc(ax, f(v), y6, 1.0, 'limite', fill=False)
text(ax, 8, 50, '=', 'resultat', 'l')
text(ax, 8, 31, '≠', 'limite', 'l')
text(ax, f(3) + 4, 12, r'$3 \notin (6)$', 'limite', 's')
save(fig, '56-092')
