import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for k in range(6):
    box(ax, 2 + k * 14.4, 30, 13, 10, 'sujet' if k == 0 else 'autre', label=r'$\{%d,%d\}$' % (k, k + 6), size='s')
brace(ax, 2, 15, 41, 'sujet', down=False)
text(ax, 2, 47, r'$H$ : 2 éléments', 'sujet', 's', ha='left')
brace(ax, 2, 84, 29, 'autre', label='G/H : 6 classes')
text(ax, 44, 10, r'$12=2\times6$ ; 3 ne divise pas 2', 'encre', 's')
text(ax, 44, 3, '3 divise 6', 'resultat', 'm')
save(fig, '60-116')
