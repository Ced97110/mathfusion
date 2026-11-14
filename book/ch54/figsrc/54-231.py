import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
def row(y, role, caption, f, g, h, dy=14):
    text(ax, 44, y + dy, caption, role, 's')
    box(ax, 2, y, 26, 10, role, label=f, size='m')
    text(ax, 30.5, y + 5, '=', 'encre', 'm')
    box(ax, 33, y, 24, 10, role, label=g, size='m')
    text(ax, 59.5, y + 5, r'$\times$', 'encre', 'm')
    box(ax, 62, y, 24, 10, role, label=h, size='m')
row(62, 'sujet', r'dans $\mathbb{Z}[x]$ : $f=g\,h$', r'$x^2-1$', r'$x-1$', r'$x+1$')
row(22, 'resultat', r'modulo 3 : $\bar{f}=\bar{g}\,\bar{h}$', r'$x^2+2$', r'$x-1$', r'$x+1$', dy=-17)
for cx in (45, 74):
    arrow(ax, (cx, 61), (cx, 33.5), 'varie')
text(ax, 20, 47, 'modulo 3', 'varie', 's')
brace(ax, 33, 57, 21, 'resultat', label='degré 1', depth=1.6)
brace(ax, 62, 86, 21, 'resultat', label='degré 1', depth=1.6)
save(fig, '54-231')
