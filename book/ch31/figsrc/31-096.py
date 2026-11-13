import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 26, 66, 8, -2, 2, step=1, arrow_right=False)
line(ax, [(f(0), 12), (f(0), 52)], 'fixe', lw=0.6, dash=True)
rows = [('sec', 1.6667, False, '1,6667'), ('tan', 1.3333, True, '± 1,3333'), ('cosec', 1.25, True, '± 1,25'), ('cotan', 0.75, True, '± 0,75')]
for i, (n, v, two, lab) in enumerate(rows):
    y = 46 - i * 10
    text(ax, 3, y, n, 'sujet' if not two else 'varie', 'm', ha='left')
    disc(ax, f(v), y, 1.8, 'sujet' if not two else 'varie')
    if two: disc(ax, f(-v), y, 1.8, 'varie')
    text(ax, 71, y, lab, 'sujet' if not two else 'varie', 's', ha='left')
text(ax, 44, 56, 'un point ou deux points', 'encre', 'm') if False else None
save(fig, '31-096')
