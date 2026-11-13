import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 5, 48, 34, 10, 'sujet', label=r'$2x=0$'); box(ax, 49, 48, 34, 10, 'sujet', label=r'$x=4$')
arrow(ax, (22, 47), (22, 31), 'varie'); arrow(ax, (66, 47), (66, 31), 'varie')
text(ax, 25, 39, r'$\div$ 0', 'varie', 'm', ha='left'); text(ax, 69, 39, r'$\times$ 0', 'varie', 'm', ha='left')
box(ax, 5, 20, 34, 10, 'limite', label='aucun résultat', size='s'); box(ax, 49, 20, 34, 10, 'limite', label=r'$0=0$ : sans valeur', size='s')
box(ax, 4, 3, 80, 10, 'resultat', label=r'« non nul » écarte les deux défauts', size='s')
save(fig, '16-054')
