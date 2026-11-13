import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
# Z/2Z : the four programs a + b x and the table of values (p(0), p(1))
table = [((a, b), ((a + b * 0) % 2, (a + b * 1) % 2)) for a in (0, 1) for b in (0, 1)]
assert sorted(v for _, v in table) == [(0, 0), (0, 1), (1, 0), (1, 1)]   # all 4 maps are reached
text(ax, 11, 76, r'$a$', 'varie', 'm')
text(ax, 23, 76, r'$b$', 'varie', 'm')
text(ax, 45, 76, r'$p(0)$', 'sujet', 'm')
text(ax, 58, 76, r'$p(1)$', 'sujet', 'm')
y = 60
for (a, b), (v0, v1) in table:
    box(ax, 6, y, 10, 9, 'varie', label=str(a), size='m')
    box(ax, 18, y, 10, 9, 'varie', label=str(b), size='m')
    arrow(ax, (29.5, y + 4.5), (38.5, y + 4.5), 'varie')
    box(ax, 40, y, 10, 9, 'sujet', label=str(v0), size='m')
    box(ax, 53, y, 10, 9, 'sujet', label=str(v1), size='m')
    y -= 12
# bracket: these are all the maps Z/2Z -> Z/2Z
line(ax, [(67, 63), (69, 63), (69, 21), (67, 21)], 'resultat', lw=1.0)
text(ax, 78, 42, 'les 4 tableaux possibles', 'resultat', 's', rot=90)
text(ax, 44, 12, r'donc toute application est $a+bx$', 'resultat', 's', weight='bold')
text(ax, 44, 5, r'$x^2$ et $x$ : mêmes valeurs 0 et 1', 'encre', 's')
save(fig, '55-135')
