import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
box(ax, 2, 26, 14, 10, 'sujet', label='a = 3')
for i in range(4):
    x = 18 + i * 14
    box(ax, x, 26, 12, 10, 'varie', label='+ 4')
    text(ax, x + 6, 40, str(i + 1), 'varie', 's')
    arrow(ax, (x - 2, 31), (x, 31), 'varie')
box(ax, 74, 26, 12, 10, 'resultat', label='19')
arrow(ax, (72.2, 31), (74, 31), 'varie')
brace(ax, 18, 72, 24, 'varie', label='k = 4 pas de m = 4')
text(ax, 44, 8, r'$k = (b-a)\,s = 1 \times 4 = 4$', 'sujet', 'm')
save(fig, '52-189')
