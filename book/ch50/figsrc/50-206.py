import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
assert [d for d in (1, 3, 9) if 11 % d == 0] == [1] and 9 * 11 // 1 == 99
cols = [34, 48, 62]
text(ax, 2, 66, 'diviseurs de 9', 'fixe', 's', ha='left'); text(ax, 2, 48, 'diviseurs de 11', 'fixe', 's', ha='left')
for x, t, r in zip(cols, ['1', '3', '9'], ['resultat', 'sujet', 'sujet']): box(ax, x, 62, 11, 8, r, label=t, size='l')
for x, t, r in zip(cols[:2], ['1', '11'], ['resultat', 'autre']): box(ax, x, 44, 11, 8, r, label=t, size='l')
line(ax, [(39.5, 62), (39.5, 52)], 'resultat', lw=1.4)
text(ax, 44, 36, r'$|H\cap K|=1$', 'resultat', 'l', weight='bold')
arrow(ax, (44, 31), (44, 26), 'varie')
text(ax, 44, 21, r'$|HK|=9\times 11/1=99$', 'encre', 'm')
text(ax, 44, 10, r'$HK=G$ : 99 éléments', 'resultat', 'l', weight='bold')
save(fig, '50-206')
