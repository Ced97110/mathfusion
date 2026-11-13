import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 40, 45, 'coefficients k : les nombres de ℝ', 'fixe', 's')
f = numberline(ax, 8, 68, 28, -2, 3, step=1, labels=True, arrow_right=True)
for v in (-1, 0.5, 1.5, 2):
    disc(ax, f(v), 28, 1.5, 'varie')
text(ax, f(0.5), 34, '½', 'varie', 'm')
text(ax, f(1.5), 34, '1,5', 'varie', 'm')
text(ax, 80, 28, 'ℝ', 'sujet', 'xl', weight='bold')
text(ax, 44, 10, 'k × v : k vient de ℝ', 'varie', 'm')
save(fig, '57-030')
