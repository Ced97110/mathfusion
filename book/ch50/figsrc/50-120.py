import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 9, 40.5, '$Q$', 'sujet', 'm'); text(ax, 9, 16.5, r'$P_j$', 'autre', 'm')
for x, l in [(20, '$e$'), (32, r'$s_B$')]:
    box(ax, x, 36, 12, 9, 'sujet', label=l)
    box(ax, x, 12, 12, 9, 'autre', label=l)
    arrow(ax, (x + 6, 36), (x + 6, 21), 'varie')
text(ax, 9, 28.5, r'$Q\subseteq P_j$', 'encre', 's')
text(ax, 66, 40.5, r'$p^m=2$ éléments', 'sujet', 's')
text(ax, 66, 16.5, r'$p^m=2$ éléments', 'autre', 's')
box(ax, 52, 24.5, 32, 8, 'resultat', label=r'donc $Q=P_j$', size='s')
text(ax, 44, 5, r'premier lemme : $x\in P_j$ pour $x\in Q$', 'varie', 's')
save(fig, '50-120')
