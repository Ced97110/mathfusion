import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 68, r'$(fg)(s)=f(s)g(s)$', 'encre', 'm')
f = [2, 2, 2]; g = [1, 0, 2]
for i, x in enumerate((4, 31.5, 59)):
    box(ax, x, 52, 25, 10, 'sujet', label=f'$f({i})={f[i]}$', size='s')
    text(ax, x + 12.5, 48.5, r'$\times$', 'varie', 'm')
    box(ax, x, 34, 25, 11, 'autre', label=f'$g({i})={g[i]}$', size='s')
    arrow(ax, (x + 12.5, 34), (x + 12.5, 25), 'varie')
    box(ax, x, 10, 25, 15, 'resultat', label=f'$(fg)({i})$' + f'\n{f[i]} × {g[i]} = {(f[i] * g[i]) % 3}', size='s')
save(fig, '55-020')
