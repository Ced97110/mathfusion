import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r'chiffré $c = 17$ ; message cherché : $8$', 'fixe', 's')
def col(x, titre, mod, d, prod, res, role):
    text(ax, x + 19, 62, titre, role, 'm', weight='bold')
    box(ax, x, 44, 38, 11, 'fixe', label=rf'$e \times d = 3 \times {d}$', size='s')
    text(ax, x + 19, 38, prod, 'fixe', 's')
    arrow(ax, (x + 19, 34), (x + 19, 29), role)
    box(ax, x, 15, 38, 13, role, label=res, size='m')
col(2, 'modulo 55', 55, 37, r'$111 = 2 \times 55 + 1$', r'$17^{37} \equiv 52$', 'limite')
col(48, 'modulo 40', 40, 27, r'$81 = 2 \times 40 + 1$', r'$17^{27} \equiv 8$', 'resultat')
text(ax, 21, 9, r'$52 \neq 8$ : faux', 'limite', 's')
text(ax, 67, 9, r'$8 = 8$ : bon', 'resultat', 's')
save(fig, '53-160')
