import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
text(ax, 22, 93, r'$156 \div 12$', 'sujet', 'l')
text(ax, 65, 93, r'$x^3-2x^2+4 \div (x-1)$', 'autre', 'm')
line(ax, [(44, 8), (44, 88)], 'fixe', dash=True)
left = [(72, '156'), (50, '36'), (28, '0')]
right = [(72, '$x^3-2x^2+4$\ndegré 3'), (54, '$-x^2+4$\ndegré 2'), (36, '$-x+4$\ndegré 1'), (18, '$3$\ndegré 0')]
for y, lab in left:
    box(ax, 8, y, 28, 11, 'sujet', label=lab, size='m')
for (ya, _), (yb, _) in zip(left[:-1], left[1:]):
    arrow(ax, (22, ya), (22, yb + 11.5), 'varie')
for y, lab in right:
    box(ax, 48, y, 36, 11, 'autre', label=lab, size='s')
for (ya, _), (yb, _) in zip(right[:-1], right[1:]):
    arrow(ax, (66, ya), (66, yb + 11.5), 'varie')
text(ax, 44, 4, 'chaque flèche : − un multiple du diviseur', 'varie', 's')
save(fig, '54-141')
