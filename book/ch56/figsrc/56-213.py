import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = lambda v: 14 + v * 1.9
y6, y12 = 38, 18
text(ax, 44, 56, '(12) ⊂ (6)', 'encre', 'l')
text(ax, 2, y6, '(6)', 'autre', 's', ha='left')
text(ax, 2, y12, '(12)', 'sujet', 's', ha='left')
for v in range(0, 37, 6):
    text(ax, f(v), y6 + 4.5, str(v), 'autre', 's')
    absent = v % 12 != 0
    disc(ax, f(v), y6, 1.0, 'varie' if absent else 'autre')
    if absent:
        disc(ax, f(v), y12, 1.0, 'fixe', fill=False)
    else:
        disc(ax, f(v), y12, 1.0, 'sujet')
        line(ax, [(f(v), y12 + 1.2), (f(v), y6 - 1.2)], 'fixe', lw=0.6, dash=True)
text(ax, 44, 10, '6, 18, 30 : dans (6), pas dans (12)', 'varie', 's')
save(fig, '56-213')
