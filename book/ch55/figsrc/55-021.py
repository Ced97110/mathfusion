import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
f = [1, 2, 0]; g = [2, 2, 1]
text(ax, 10, 42, r'$f+g$', 'sujet', 'm')
text(ax, 10, 22, r'$g+f$', 'autre', 'm')
for i, x in enumerate((20, 42, 64)):
    box(ax, x, 36.5, 20, 11, 'sujet', label=f'${f[i]}+{g[i]}={(f[i] + g[i]) % 3}$', size='s')
    text(ax, x + 10, 32, '=', 'resultat', 'l')
    box(ax, x, 16.5, 20, 11, 'autre', label=f'${g[i]}+{f[i]}={(f[i] + g[i]) % 3}$', size='s')
box(ax, 4, 2, 80, 10, 'fixe', label='entrées 0, 1, 2, dans $F$', size='s')
save(fig, '55-021')
