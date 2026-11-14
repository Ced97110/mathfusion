import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 88, r'$G/K$ : 6 éléments, $K$={0, 6}', 'sujet', 'm')
w, g, x0 = 10, 2, 9
for i in range(6):
    r = 'autre' if i % 2 == 0 else 'sujet'
    box(ax, x0 + i * (w + g), 69, w, 9, r, label=str(i), size='s')
text(ax, 44, 61, r'violet : $H/K$, 3 éléments', 'autre', 's')
arrow(ax, (31, 56), (31, 47), 'fixe'); arrow(ax, (75, 56), (75, 47), 'fixe')
for i in range(2):
    box(ax, 8 + i * 12, 35, 10, 10, 'fixe', fill=True)
    box(ax, 62 + i * 12, 35, 10, 10, 'fixe', fill=True)
text(ax, 20, 28, r'$(G/K)/(H/K)$ : 2', 'fixe', 's')
text(ax, 74, 28, r'$G/H$ : 2', 'fixe', 's')
text(ax, 44, 40, r'$2 = 2$', 'fixe', 'l', weight='bold')
box(ax, 8, 4, 72, 16, 'limite', label='compter ne suffit pas :\nisomorphisme non montré', size='s', dash=True)
save(fig, '48-162')
