import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

# x^4 = x * x^3 = x * (1 + x) = x + x^2, reste noté (coef. de 1, de x, de x^2)
assert (0, 1, 1) == (0, 1, 1)
fig, ax = canvas(96)
text(ax, 2, 88, 'position', 'fixe', 's', ha='left')
bitrow(fig, ax, 58, 88, '0123456', 'fixe', 'l', 5)
text(ax, 2, 77, 'erreur x⁴', 'limite', 'm', ha='left')
word = '0000100'
brow(fig, ax, 58, 77, word, roles=['limite' if c == '1' else 'fixe' for c in word])
box(ax, 20, 58, 48, 10, 'fixe', label=r'règle : $x^3 = 1 + x$', size='s')
arrow(ax, (44, 57), (44, 51), 'varie')
text(ax, 44, 46, r'$x^4 = x \times x^3 = x \times (1 + x)$', 'encre', 's')
text(ax, 44, 38, r'$= x + x^2$', 'varie', 'l')
xs, p = brow(fig, ax, 44, 25, '011', role='resultat')
for x, t in zip(xs, ['1', 'x', 'x²']):
    text(ax, x, 18.5, t, 'fixe', 's')
text(ax, 44, 9, 'reste = syndrome de l’erreur', 'resultat', 's')
save(fig, '68-197')
