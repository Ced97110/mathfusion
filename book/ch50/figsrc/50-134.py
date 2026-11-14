import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$G$ : 8 éléments', 'fixe', 'm')
for i in range(8): box(ax, 8 + i * 9.5, 40, 9, 9, 'fixe')
text(ax, 44, 30, r'$C$(réflexion) : 4 éléments', 'sujet', 'm')
for i in range(8):
    box(ax, 8 + i * 9.5, 14, 9, 9, 'sujet' if i < 4 else 'limite', fill=i < 4, dash=i >= 4)
brace(ax, 8, 8 + 3 * 9.5 + 9, 14, 'sujet', label='commutent avec elle')
brace(ax, 8 + 4 * 9.5, 8 + 7 * 9.5 + 9, 14, 'limite', label='ne commutent pas')
text(ax, 44, 4, r'$4 < 8$ : $C$ plus petit que $G$', 'resultat', 's')
save(fig, '50-134')
