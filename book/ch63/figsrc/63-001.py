import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 40, 66, 14, 'sujet', label=r'$(3+\sqrt{2})^2 = 11+6\sqrt{2}$')
box(ax, 2, 6, 66, 14, 'varie', label=r'$(3-\sqrt{2})^2 = 11-6\sqrt{2}$')
box(ax, 72, 40, 14, 14, 'resultat', label='vrai', size='s')
box(ax, 72, 6, 14, 14, 'resultat', label='vrai', size='s')
arrow(ax, (20, 39), (20, 21), 'varie')
text(ax, 24, 30, r'$\sqrt{2}\mapsto-\sqrt{2}$', 'varie', 'm', ha='left')
save(fig, '63-001')
