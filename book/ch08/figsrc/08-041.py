import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 6, 60, 30, 10, 'fixe', label='3 = 3,00', size='m')
arrow(ax, (36, 65), (46, 65), 'varie')
box(ax, 46, 60, 36, 10, 'resultat', label='3,00 ÷ 4 = 0,75', size='m')
f = numberline(ax, 8, 74, 36, 0, 3, step=0.75, arrow_right=False)
for i in range(4):
    arrow(ax, (f(.75 * i) + .5, 38), (f(.75 * (i + 1)) - .5, 38), 'varie', curve=-0.6)
brace(ax, f(0), f(3), 27, 'varie', '4 pas égaux de 0,75')
text(ax, 44, 10, r'$4\times 0{,}75 = 3$', 'resultat', 'l')
save(fig, '08-041')
