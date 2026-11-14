import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
c = 70/5625
box(ax, 6, 43, 5625*c, 8, 'resultat', label=r'$75^2$ = 5625')
text(ax, 6, 35, 'addition simple : 2925 ≠ 5625', 'limite', 'm', ha='left')
box(ax, 6, 25, 900*c, 8, 'sujet', label='900')
box(ax, 6 + 900*c, 25, 2025*c, 8, 'autre', label='2025')
text(ax, 6, 16, 'une autre règle : 5625', 'resultat', 'm', ha='left')
box(ax, 6, 6, 900*c, 8, 'sujet', label='900')
box(ax, 6 + 900*c, 6, 2700*c, 8, 'varie', label=r'$2\times30\times45$')
box(ax, 6 + 3600*c, 6, 2025*c, 8, 'autre', label='2025')
save(fig, '34-005')
