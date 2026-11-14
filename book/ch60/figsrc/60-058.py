import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 44, 50, 'idéaux : (2) ⊇ (6)', 'encre', 'm')
f = numberline(ax, 12, 70, 12, 0, 12, step=1, every=2)
text(ax, 12, 40, '(2) : multiples de 2', 'sujet', 'm', ha='left')
text(ax, 12, 18, '(6) : multiples de 6', 'autre', 'm', ha='left')
for v in range(0, 13, 2):
    disc(ax, f(v), 34, 1.6, 'sujet')
for v in (0, 6, 12):
    disc(ax, f(v), 23, 1.6, 'autre')
    line(ax, [(f(v), 25), (f(v), 32)], 'fixe', lw=0.6, dash=True)
save(fig, '60-058')
