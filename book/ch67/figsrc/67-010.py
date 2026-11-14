import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
els = ['0', '1', r'$\alpha$', r'$\alpha+1$']
roles = ['fixe', 'fixe', 'sujet', 'resultat']
for i in range(4):
    box(ax, 6 + i * 20, 36, 16, 12, roles[i], label=els[i])
arrow(ax, (54, 48), (74, 48), 'varie', curve=-0.9)
text(ax, 64, 62, r'$\alpha\times\alpha=\alpha^2$', 'varie', 'm')
brace(ax, 6, 42, 36, 'fixe', label='déjà connus')
box(ax, 8, 8, 72, 13, 'sujet', label=r'règle : $\alpha^2=\alpha+1$', size='l')
save(fig, '67-010')
