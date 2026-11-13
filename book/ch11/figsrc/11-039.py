import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
vals = ['1 000', '100', '10', '1']; exps = [3, 2, 1, 0]
for i in range(4):
    x = 3 + i * 22
    box(ax, x, 26, 16, 12, 'resultat' if i == 3 else 'fixe', label=vals[i], size='l')
    text(ax, x + 8, 20, r'$10^{%d}$' % exps[i], 'resultat' if i == 3 else 'fixe', 'm')
    if i < 3:
        arrow(ax, (x + 17, 32), (x + 24, 32), 'varie')
        text(ax, x + 20.5, 36.5, '÷ 10', 'varie', 's')
text(ax, 69, 12, 'base : zéro facteur 10', 'resultat', 's')
text(ax, 44, 48, 'base = 1 = 10 puissance zéro', 'encre', 'm')
save(fig, '11-039')
