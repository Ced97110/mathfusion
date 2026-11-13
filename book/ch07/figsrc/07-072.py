import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
F = r'$\frac{1}{2}$'
for x, s, r in [(16, F, 'sujet'), (28, '+', 'fixe'), (40, F, 'sujet'), (52, r'$\times$', 'varie'), (64, F, 'varie')]:
    text(ax, x, 72, s, r, 'l' if s != F else 'l')
brace(ax, 35, 70, 66, 'varie', label='1er : on multiplie')
arrow(ax, (30, 53), (24, 44), 'resultat')
arrow(ax, (58, 53), (66, 44), 'limite')
text(ax, 24, 36, r'$\frac{1}{2} + \frac{1}{4} = \frac{3}{4}$', 'resultat', 'm')
text(ax, 66, 36, r'$1 \times \frac{1}{2} = \frac{1}{2}$', 'limite', 'm')
text(ax, 24, 22, 'on multiplie d\'abord', 'resultat', 's', weight='bold')
text(ax, 66, 22, 'on additionne d\'abord', 'limite', 's', weight='bold')
text(ax, 24, 12, 'valeur juste', 'resultat', 's')
text(ax, 66, 12, 'valeur fausse', 'limite', 's')
save(fig, '07-072')
