import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for x, role in [(13, 'sujet'), (45, 'sujet'), (71, 'resultat')]:
    box(ax, x - 7, 50, 14, 10, role, label='R', size='l')
text(ax, 29, 55, '·', 'encre', 'l'); text(ax, 58, 55, '=', 'encre', 'l')
f = numberline(ax, 14, 62, 26, 0, 3, arrow_right=False)
arrow(ax, (f(0), 29), (f(1), 29), 'varie', curve=-0.6); text(ax, (f(0) + f(1)) / 2, 36, r'$r$', 'varie', 'm')
arrow(ax, (f(1), 29), (f(3), 29), 'varie', curve=-0.6); text(ax, (f(1) + f(3)) / 2, 42, r'$r^2$', 'varie', 'm')
brace(ax, f(0), f(3), 19, 'resultat', label=r'3 quarts de tour : $r^3$', size='m')
save(fig, '47-154')
