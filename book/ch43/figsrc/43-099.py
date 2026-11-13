import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(94)
f = numberline(ax, 10, 70, 40, 0, 5, labels=False)
for v in (1, 2, 4, 5):
    line(ax, [(f(v), 12), (f(v), 84)], 'fixe', lw=0.6, dash=True)
line(ax, [(f(3), 12), (f(3), 84)], 'sujet', lw=1.6)
for y in (70, 28):
    arrow(ax, (f(3), y + (-2.2 if y > 40 else 2.2)), (f(3), 40 + (2.4 if y > 40 else -2.4)), 'varie')
    disc(ax, f(3), y, 1.8, 'varie')
disc(ax, f(3), 40, 1.8, 'resultat')
text(ax, f(3) + 3, 70, r'$(3\ ;\ 5)$', 'varie', 's', ha='left')
text(ax, f(3) + 3, 28, r'$(3\ ;\ -2)$', 'varie', 's', ha='left')
text(ax, f(3) + 3, 36, '3', 'resultat', 's', ha='left')
text(ax, 80, 44, r'$l$', 'fixe', 'm')
text(ax, f(3), 89, 'fibre au-dessus de 3', 'sujet', 's')
save(fig, '43-099')
