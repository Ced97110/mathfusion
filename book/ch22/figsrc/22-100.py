import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y, h = 36, 9
def pair(x, cw, c, role='varie'):
    box(ax, x, y, cw, h, role, label=c, size='s'); box(ax, x + cw, y, 6.5, h, 'fixe', label=r'$\sqrt{3}$', size='s'); return x + cw + 6.5
x = pair(3, 7, '4'); text(ax, x + 1.8, y + h / 2, '+', 'encre', 'm')
x = pair(x + 3.6, 7, '8')
arrow(ax, (x + 1.5, y + h / 2), (x + 5.5, y + h / 2), 'varie')
x = pair(x + 7, 12, '4+8')
arrow(ax, (x + 1.5, y + h / 2), (x + 5.5, y + h / 2), 'varie')
pair(x + 7, 9, '12', 'resultat')
text(ax, 44, 29, 'le radical ne change pas', 'fixe', 's')
text(ax, 44, 20, 'même calcul, autres nombres', 'fixe', 's')
box(ax, 18, 5, 52, 10, 'autre', label=r'$5\sqrt{3}+2\sqrt{3}=7\sqrt{3}$')
save(fig, '22-100')
