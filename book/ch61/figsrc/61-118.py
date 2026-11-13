import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
labs = ['1', r'$u$', r'$u^2$', '…', r'$u^n$']; co = [r'$a_0$', r'$a_1$', r'$a_2$', '…', r'$a_n$']
for i in range(5):
    x = 4 + i * 17
    box(ax, x, 34, 14, 11, 'varie', label=labs[i], size='m')
    text(ax, x + 7, 51, co[i], 'fixe', 'm')
text(ax, 44, 58, 'coefficients', 'fixe', 's')
brace(ax, 4, 82, 32, 'varie', label=r'$n+1$ éléments', size='s')
box(ax, 4, 6, 38, 11, 'sujet', label=r'espace de dimension $n$', size='s')
arrow(ax, (43, 11.5), (49, 11.5), 'resultat', lw=1.2)
box(ax, 50, 6, 34, 11, 'resultat', label=r'liés : somme = 0', size='s')
save(fig, '61-118')
