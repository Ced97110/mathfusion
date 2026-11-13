import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'dans $\mathbb{Z}/5$', 'fixe', 's')
for k, (n, r) in enumerate(((1, 'sujet'), (4, 'sujet'), (2, 'limite'), (3, 'limite'))):
    disc(ax, 14 + k * 20, 56, 5.5, r, label=str(n), size='l')
brace(ax, 8, 40, 49, 'sujet', 'carrés', down=True); brace(ax, 48, 80, 49, 'limite', 'non-carrés', down=True)
box(ax, 4, 14, 36, 14, 'sujet', label=r'diag$(1,1)$'); box(ax, 48, 14, 36, 14, 'limite', label=r'diag$(1,2)$')
text(ax, 22, 8, r'discriminant $1$', 'sujet', 's'); text(ax, 66, 8, r'discriminant $2$', 'limite', 's')
text(ax, 44, 21, r'$\neq$', 'limite', 'xl')
text(ax, 44, 33, 'discriminant différent', 'limite', 's'); text(ax, 44, 38, 'donc pas congruentes', 'limite', 's')
save(fig, '71-205')
