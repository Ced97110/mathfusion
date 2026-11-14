import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, 'Mot de 4 bits : 1 0 1 1', 'sujet', 's')
bits = [1, 0, 1, 1]
terms = [r'$1$', r'$0$', r'$x^2$', r'$x^3$']
xs = [14 + i * 20 for i in range(4)]
for i, (x, b, t) in enumerate(zip(xs, bits, terms)):
    box(ax, x - 7, 52, 14, 10, 'sujet', label=str(b), size='m')
    text(ax, x, 47, rf'rang {i}', 'fixe', 's')
    arrow(ax, (x, 44), (x, 38), 'varie')
    box(ax, x - 7, 27, 14, 10, 'fixe' if b == 0 else 'varie', label=t if b else r'$0\cdot x$', size='s')
box(ax, 8, 8, 72, 12, 'resultat', label=r'$1+x^2+x^3$', size='m')
arrow(ax, (44, 26), (44, 21), 'resultat')
save(fig, '54-280')
