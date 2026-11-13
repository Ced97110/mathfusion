import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
xs = [2, 34, 66]
labs = ['2  1\n1  1', '1  0\n1  1', '1  0\n0  1']
roles = ['sujet', 'fixe', 'resultat']
for x, l, r in zip(xs, labs, roles): box(ax, x, 14, 20, 16, r, label=l, size='l')
text(ax, 12, 36, r'$A$', 'sujet', 'l'); text(ax, 76, 36, r'$D$', 'resultat', 'l')
for x, l in zip([22, 54], ['L1 − L2', 'L2 − L1']):
    arrow(ax, (x+1, 22), (x+11, 22), 'varie'); text(ax, x+6, 27, l, 'varie', 's')
brace(ax, 23, 65, 11, 'varie', 'chaque étape : une transvection', size='s')
save(fig, '73-050')
