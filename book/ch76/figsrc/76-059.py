import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
labs = [r'$\emptyset$', r'$\{1\}$', r'$\{2\}$', r'$\{1,2\}$']
mons = ['1', r'$e_1$', r'$e_2$', r'$e_1\wedge e_2$']
text(ax, 2, 49, r'base $\mathcal{P}(N)$', 'sujet', 's', ha='left')
text(ax, 2, 22, 'monômes', 'resultat', 's', ha='left')
for i in range(4):
    x = 24 + i * 16
    box(ax, x, 44, 14, 10, 'sujet', label=labs[i], size='s')
    arrow(ax, (x + 7, 43), (x + 7, 28), 'varie', both=True)
    box(ax, x, 17, 14, 10, 'resultat', label=mons[i], size='s')
box(ax, 14, 2, 60, 9, 'resultat', label=r'4 indépendants, $4=2^2$', size='s')
save(fig, '76-059')
