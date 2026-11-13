import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for y, a, b in ((56, '6$x$', '6 fois $x$'), (40, '$ab$', '$a$ fois $b$')):
    box(ax, 6, y - 6, 22, 12, 'sujet', label=a, size='l')
    arrow(ax, (30, y), (46, y), 'varie')
    box(ax, 48, y - 6, 34, 12, 'varie', label=b)
line(ax, [(2, 28), (86, 28)], 'fixe', lw=0.5, dash=True)
text(ax, 22, 21, '$x$ = 3 :', 'encre', 'm')
box(ax, 36, 14, 20, 12, 'resultat', label='6$x$ = 18')
box(ax, 62, 14, 20, 12, 'limite', label='pas 63')
save(fig, '12-028')
