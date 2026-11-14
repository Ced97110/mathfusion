import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = numberline(ax, 8, 76, 35, -180, 180, step=30, every=6, arrow_right=False)
for v in (-90, 30, 150):
    line(ax, [(f(v), 20), (f(v), 50)], 'resultat', dash=True)
    disc(ax, f(v), 50, 2.2, 'varie')
    disc(ax, f(v), 20, 2.2, 'autre')
    text(ax, f(v), 56, f'{v}°'.replace('-', '−'), 'varie', 's')
    text(ax, f(v), 14, f'{v}°'.replace('-', '−'), 'autre', 's')
text(ax, 2, 50, 'chemin 1', 'varie', 's', ha='left')
text(ax, 2, 20, 'chemin 2', 'autre', 's', ha='left')
text(ax, 44, 5, 'les mêmes 3 angles', 'resultat', 's')
save(fig, '32-120')
