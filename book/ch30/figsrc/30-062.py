import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 4, 26, 32, 12, 'sujet', label='cotan 60°', size='m'); text(ax, 20, 44, 'livre français', 'sujet', 's')
box(ax, 52, 26, 32, 12, 'autre', label='cot 60°', size='m'); text(ax, 68, 44, 'livre anglais', 'autre', 's')
text(ax, 44, 32, '=', 'resultat', 'l')
box(ax, 26, 4, 36, 10, 'resultat', label='≈ 0,577', size='m')
arrow(ax, (20, 25), (36, 14.8), 'resultat'); arrow(ax, (68, 25), (52, 14.8), 'resultat')
save(fig, '30-062')
