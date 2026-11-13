import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = lambda v: 16 + v * 2.2
y5, y15 = 42, 22
text(ax, 44, 58, r'$5 \mid 15 \Leftrightarrow (15) \subseteq (5)$', 'encre', 'm')
text(ax, 2, y5, '(5)', 'autre', 's', ha='left')
text(ax, 2, y15, '(15)', 'sujet', 's', ha='left')
for v in range(0, 31, 5):
    text(ax, f(v), y5 + 4.5, str(v), 'autre', 's')
    if v % 15 == 0:
        disc(ax, f(v), y5, 1.0, 'autre')
        disc(ax, f(v), y15, 1.0, 'sujet')
        line(ax, [(f(v), y15 + 1.2), (f(v), y5 - 1.2)], 'fixe', lw=0.6, dash=True)
    else:
        disc(ax, f(v), y5, 1.0, 'autre')
disc(ax, f(5), y15, 1.0, 'limite', fill=False)
text(ax, f(5) + 6, y15 - 6, r'$5 \notin (15)$', 'limite', 's')
text(ax, 50, 8, 'les multiples de 15 sont multiples de 5', 'resultat', 's')
save(fig, '56-091')
