import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 50, 'La moitié d’un nombre est 15', 'encre', 'm')
cols = [(3, 40, 'la moitié d’un nombre', r'$x \div 2$'), (46, 16, 'est', r'$=$'), (65, 20, '15', r'$15$')]
for x, w_, a, b in cols:
    box(ax, x, 32, w_, 8, 'fixe', label=a, size='s')
    arrow(ax, (x + w_ / 2, 32), (x + w_ / 2, 22), 'varie')
    box(ax, x, 14, w_, 8, 'sujet', label=b)
text(ax, 44, 6, 'plus aucun mot sans signe', 'resultat', 's')
save(fig, '16-108')
