import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
a, b = (1, 2, 1), (0, 1, -1)
cross = (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
assert cross == (-3, 1, 1)
box(ax, 4, 72, 36, 9, 'sujet', label=r'$a=(1,2,1)$')
box(ax, 48, 72, 36, 9, 'autre', label=r'$b=(0,1,-1)$')
text(ax, 48, 66, r'$a\times b$ : case par case', 'varie', 's', ha='left')
calc = [(r'$2\times(-1)-1\times1=-3$', 'x'), (r'$1\times0-1\times(-1)=1$', 'y'), (r'$1\times1-2\times0=1$', 'z')]
for (s, _), y in zip(calc, [52, 40, 28]):
    box(ax, 10, y, 68, 9, 'varie', label=s)
arrow(ax, (44, 71), (44, 62), 'varie')
box(ax, 14, 11, 60, 9, 'resultat', label=r'$a\times b=(-3,1,1)$')
arrow(ax, (44, 27), (44, 21), 'resultat')
text(ax, 44, 5, r'plan de $W$ : $-3x+y+z=0$', 'resultat', 'm')
save(fig, '58-129')
