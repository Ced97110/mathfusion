import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 15, 57, 'reste 2 par 3', 'sujet', 's')
text(ax, 42, 57, 'reste 4 par 5', 'autre', 's')
text(ax, 70, 57, 'les deux : 14, 29, 44', 'resultat', 's')
f = numberline(ax, 6, 78, 18, 0, 45, labels=True, every=15, arrow_right=False)
for v in range(2, 46, 3): disc(ax, f(v), 24, 0.9, 'sujet')
for v in range(4, 46, 5): disc(ax, f(v), 29, 0.9, 'autre')
for v in (14, 29, 44):
    line(ax, [(f(v), 18), (f(v), 33)], 'resultat', lw=0.7, dash=True)
    disc(ax, f(v), 35, 1.6, 'resultat')
arrow(ax, (f(14), 37.5), (f(29), 37.5), 'varie', curve=-0.4)
text(ax, f(21.5), 47, '+ 15 = 3 × 5', 'varie', 's')
save(fig, '52-184')
