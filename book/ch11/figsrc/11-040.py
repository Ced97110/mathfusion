import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 54, r'$d$ = 0,1 = $10^{-1}$', 'sujet', 'xl')
vals = ['1', '0,1', '0,01', '0,001']; exps = [None, -1, -2, -3]
for i in range(4):
    x = 3 + i * 22
    box(ax, x, 24, 16, 12, 'sujet' if i == 1 else 'fixe', label=vals[i], size='l')
    if exps[i] is not None:
        text(ax, x + 8, 18, r'$10^{%d}$' % exps[i], 'sujet' if i == 1 else 'fixe', 'm')
    if i < 3:
        arrow(ax, (x + 17, 30), (x + 24, 30), 'varie')
        text(ax, x + 20.5, 34.5, '÷ 10', 'varie', 's')
text(ax, 44, 8, 'nombre positif, plus petit que 1', 'resultat', 's')
save(fig, '11-040')
