import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 44, 84, 'p ne divise pas le discriminant', 'encre', 'm')
for y, p in [(70, 2), (56, 3), (42, 5)]:
    text(ax, 3, y, rf'$p={p}$', 'sujet', 'm', ha='left')
    for i in range(6):
        disc(ax, 28 + 9 * i, y, 2.6, 'sujet')
text(ax, 44, 33, r'$f_{p}$ : six racines distinctes', 'sujet', 'm')
line(ax, [(3, 28), (85, 28)], 'fixe', lw=0.6, dash=True)
text(ax, 3, 20, r'si $p$ divisait :', 'limite', 'm', ha='left')
for i in range(5):
    x = 32.5 + 9 * i
    disc(ax, x, 20, 2.6, 'limite')
    if i == 2:
        disc(ax, x + 1.5, 20, 2.6, 'limite', fill=False)
text(ax, 44, 12, 'racine double', 'limite', 'm')
box(ax, 8, 1.5, 72, 7, 'resultat', label='Dedekind vaut pour 2, 3, 5', size='s')
save(fig, '67-207')
