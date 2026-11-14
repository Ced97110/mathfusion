import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 10, 78, 28, 0, 6, arrow_right=False)
for v in range(7): disc(ax, f(v), 35, 3.2, 'sujet' if v % 2 == 0 else 'varie')
disc(ax, f(3), 35, 4.8, 'resultat', fill=False, lw=1.6); text(ax, f(3), 45, 'le nombre 3', 'resultat', 's')
disc(ax, 8, 14, 2.4, 'sujet'); text(ax, 12, 14, 'reste 0 (pair)', 'sujet', 's', ha='left')
disc(ax, 46, 14, 2.4, 'varie'); text(ax, 50, 14, 'reste 1 (impair)', 'varie', 's', ha='left')
text(ax, 44, 6, 'pas les deux : contradiction', 'limite', 's')
save(fig, '50-109')
