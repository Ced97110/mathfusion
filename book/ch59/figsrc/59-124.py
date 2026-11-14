import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
y = 28
f = numberline(ax, 10, 70, y, 0, 20, step=1, every=10, arrow_right=False)
text(ax, 78, y, 'v', 'sujet', 's', weight='bold')
for v in (0, 10, 20):
    disc(ax, f(v), y + 8, 2.0, 'sujet')
    line(ax, [(f(v), y + 1.5), (f(v), y + 6)], 'sujet', lw=0.7)
disc(ax, f(2), y + 8, 2.0, 'limite')
line(ax, [(f(2), y + 1.5), (f(2), y + 6)], 'limite', lw=0.7)
text(ax, f(2), y - 7.5, '2', 'limite', 's', weight='bold')
text(ax, 44, y + 18, 'points de K : v = 0, 10, 20', 'sujet', 's')
text(ax, 44, 66, '(2, 2) = 2e′₂', 'encre', 'm', weight='bold')
text(ax, 44, 59, 'donc u = 0 et v = 2', 'encre', 's')
text(ax, 44, 10, '2 n’est pas multiple de 10', 'limite', 's')
text(ax, 44, 4, '(2, 2) n’est pas dans K', 'limite', 'm', weight='bold')
save(fig, '59-124')
