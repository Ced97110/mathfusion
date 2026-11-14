import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, 'trois fractions décimales', 'sujet', 'm', weight='bold')
cols = [(16, '3', '10', 'dixièmes'), (44, '35', '100', 'centièmes'), (72, '8014', '10 000', 'dix-millièmes')]
for x, n, d, nm in cols:
    text(ax, x, 40, n, 'varie', 'l', weight='bold')
    line(ax, [(x - 8, 35.5), (x + 8, 35.5)], 'encre', lw=1.0)
    box(ax, x - 9, 21, 18, 9, 'sujet', label=d, size='l', weight='bold')
    text(ax, x, 16, nm, 'sujet', 's')
text(ax, 22, 6, 'haut : un entier', 'varie', 's')
text(ax, 64, 6, 'bas : 1 et des zéros', 'sujet', 's')
fig_ = save(fig, '08-020')
