import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(50)
brace(ax, 20, 81, 40, 'sujet', label=r'0⁵ = 0 $\times$ 0 $\times$ 0 $\times$ 0 $\times$ 0', down=False, size='s')
text(ax, 10, 34, 'facteurs', 'fixe', 's')
for x0 in [20, 33, 46, 59, 72]:
    box(ax, x0, 30, 9, 8, 'sujet', fill=False, label='0', size='l')
text(ax, 10, 14, 'produit', 'fixe', 's')
for i in range(5):
    cx = 24.5 + 13 * i
    disc(ax, cx, 14, 3.5, 'resultat', fill=False, label='0', size='m', lw=1.4 if i == 4 else 0.8)
    arrow(ax, (cx, 30), (cx, 17.5), 'varie')
for i in range(4):
    arrow(ax, (28 + 13 * i, 14), (34 + 13 * i, 14), 'varie')
save(fig, '04-076')
