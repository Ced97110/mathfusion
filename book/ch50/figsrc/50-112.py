import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 3, 30, 34, 24, 'sujet'); text(ax, 20, 50, r'$P_A$', 'sujet', 'm')
disc(ax, 13, 38, 4.5, 'sujet', label='id', size='s'); disc(ax, 28, 38, 4.5, 'sujet', label=r'$s_A$', size='s')
disc(ax, 25, 12, 4.5, 'autre', label=r'$s_B$', size='s')
arrow(ax, (33, 40), (56, 45), 'varie'); arrow(ax, (30, 13), (56, 17), 'varie')
text(ax, 69, 46, r'$s_A$ : $P_A\to P_A$', 'resultat', 's'); text(ax, 69, 40, r'$s_A\in P_A$', 'resultat', 's')
text(ax, 69, 20, r'$s_B$ : $P_A\to P_C$', 'limite', 's'); text(ax, 69, 14, r'$s_B\notin P_A$', 'limite', 's')
save(fig, '50-112')
