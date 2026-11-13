import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 17, 80, r'$\mathbb{Z}$', 'autre', 'l')
text(ax, 71, 80, r'$\mathbb{Q}[x]$', 'sujet', 'l')
rows = [(62, 'le plus petit', '6', r'$x^2-1$'),
        (40, 'on divise', r'$18=3\times6+0$', r'$x^3-x=x(x^2-1)+0$'),
        (18, 'le reste', '0', '0')]
for y, mid, a, b in rows:
    box(ax, 2, y, 30, 12, 'autre', label=a)
    box(ax, 56, y, 30, 12, 'sujet', label=b)
    text(ax, 44, y + 6, mid, 'fixe', 's')
for y in (62, 40):
    arrow(ax, (17, y), (17, y - 10), 'fixe')
    arrow(ax, (71, y), (71, y - 10), 'fixe')
text(ax, 17, 10, 'mesure : la valeur', 'autre', 's')
text(ax, 71, 10, 'mesure : le degré', 'sujet', 's')
save(fig, '54-178')
