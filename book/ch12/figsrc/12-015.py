import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 2, 56, 'ligne qui s’arrête', 'limite', 's', ha='left')
y = 44
f = numberline(ax, 8, 52, y, 0, 4, every=2, arrow_right=False)
line(ax, [(52, y - 1.4), (52, y + 4)], 'limite', lw=1.4)
text(ax, 52, y + 7, 'fin de page', 'limite', 's')
disc(ax, 63, y, 1.8, 'limite', fill=False)
text(ax, 70, y - 6, '5 : pas de point', 'limite', 's')
text(ax, 2, 30, 'ligne sans fin', 'resultat', 's', ha='left')
y = 18
g = numberline(ax, 8, 63, y, 0, 5, every=5)
disc(ax, g(5), y, 1.8, 'resultat')
line(ax, [(70, y), (77, y)], 'fixe', dash=True)
text(ax, 83, y, '100', 'fixe', 's')
save(fig, '12-015')
