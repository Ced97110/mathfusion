import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def cas(y, n, c, T, N):
    text(ax, 4, y + 13, f'$n={n}$, $c={c}$ : diagonale', 'encre', 's', ha='left')
    for i in range(n):
        box(ax, 4 + i * 11, y, 9, 9, 'sujet', label=f'${c}$', size='m')
    text(ax, 60, y + 6.5, '$T=' + '+'.join([str(c)] * n) + f'={T}$', 'sujet', 's', ha='left')
    text(ax, 60, y + 2, '$N=' + r'\times'.join([str(c)] * n) + f'={N}$', 'varie', 's', ha='left')
cas(36, 2, 3, 6, 9)
cas(8, 3, 2, 6, 8)
text(ax, 44, 57, r'$T(c)=nc$ et $N(c)=c^n$', 'resultat', 'm')
save(fig, '77-094')
