import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, 'corps de départ', 'sujet', 'm')
box(ax, 30, 38, 28, 16, 'sujet', label=r'$F$', size='xl')
labs = ['fractions\nℚ', 'réels\nℝ', 'restes mod. 7\nℤ/7ℤ']
for i, l in enumerate(labs):
    x = 2 + i * 29
    box(ax, x, 4, 26, 16, 'fixe', label=l, size='s')
    arrow(ax, (44, 37), (x + 13, 21.5), 'varie')
save(fig, '62-034')
