import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(68)
f = numberline(ax, 10, 80, 20, 0, 4, step=1, labels=True, every=1, size='s')
for n in range(1, 5):
    cx = f(n)
    for k in range(n):
        box(ax, cx - 4, 24 + 7 * k, 8, 6, 'sujet', r=0.5)
text(ax, 62, 62, 'case = un facteur 5', 'sujet', 's')
brace(ax, 27.5, 82, 13, 'resultat', label='couvert par la définition', down=True, size='s')
box(ax, 6, 24, 8, 6, 'limite', fill=False, dash=True, r=0.5)
text(ax, 12, 34, 'aucun facteur', 'limite', 's')
text(ax, 10, 8, '5⁰ ?', 'limite', 'm')
text(ax, 16, 48, 'à étendre : chap. 14', 'limite', 's')
arrow(ax, (12, 45), (11, 37), 'limite')
save(fig, '04-075')
