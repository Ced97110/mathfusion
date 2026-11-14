import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
y = 30
f = numberline(ax, 8, 78, y, -3, 3, labels=False, arrow_right=False)
box(ax, f(-3), y + 4, f(0) - f(-3) - 1.5, 8, 'autre', label='N')
box(ax, f(0) + 1.5, y + 4, f(3) - f(0) - 1.5, 8, 'resultat', label='P')
disc(ax, f(0), y, 2, 'fixe', fill=False)
arrow(ax, (f(0), y - 2.6), (f(0), 21), 'fixe')
text(ax, f(0), 18, '0 ∉ P', 'resultat', 'm')
text(ax, f(0), 9, 'si 0 ∈ P, 0 serait dans N', 'limite', 's')
save(fig, '69-019')
