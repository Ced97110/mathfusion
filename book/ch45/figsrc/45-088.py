import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def rowdraw(y, title, b, a, ab):
    text(ax, 44, y + 20, title, 'encre', 'm')
    box(ax, 2, y, 20, 9, 'fixe', label=r'$b_L$ : +%d' % b, size='s')
    arrow(ax, (23, y + 4.5), (29, y + 4.5), 'varie')
    box(ax, 30, y, 20, 9, 'fixe', label=r'$a_L$ : +%d' % a, size='s')
    text(ax, 54, y + 4.5, '=', 'resultat', 'l')
    box(ax, 58, y, 28, 9, 'resultat', label=r'$(ab)_L$ : +%d' % ab, size='s')
rowdraw(34, r'$a=1$, $b=2$ : $ab=3$', 2, 1, 3)
rowdraw(8, r'$a=3$, $b=3$ : $ab=2$', 3, 3, 2)
save(fig, '45-088')
