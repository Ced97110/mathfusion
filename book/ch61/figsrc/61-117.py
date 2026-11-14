import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
o = (8, 8); k = 3.6
arrow(ax, o, (o[0] + 48, o[1]), 'fixe', lw=0.8); arrow(ax, o, (o[0], o[1] + 28), 'fixe', lw=0.8)
text(ax, o[0] + 4, o[1] - 4, 'direction de 1', 'fixe', 's', ha='left'); text(ax, o[0] + 3, o[1] + 29, r'direction de $\sqrt{2}$', 'fixe', 's', ha='left')
for (a, b), n in [((1, 0), '1'), ((3, 1), r'$u$'), ((11, 6), r'$u^2$')]:
    arrow(ax, o, (o[0] + a * k, o[1] + b * k), 'sujet', lw=1.2)
    text(ax, o[0] + a * k + 2, o[1] + b * k + 3, n, 'sujet', 'm')
text(ax, 70, 38, '3 vecteurs, 2 directions : liés', 'encre', 's', ha='center') if False else text(ax, 66, 40, '3 vecteurs, un plan : liés', 'encre', 's')
text(ax, 66, 22, 'donc', 'encre', 's'); text(ax, 66, 15, r'$u^2 - 6u + 7 = 0$', 'resultat', 'm')
save(fig, '61-117')
