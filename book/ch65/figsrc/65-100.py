import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, 'les 6 permutations des 3 racines', 'encre', 's')
text(ax, 44, 48, r'équation générale : 6 sur 6, groupe $S_3$', 'sujet', 's')
for i in range(6):
    box(ax, 6 + i * 13, 36, 11, 9, 'sujet')
text(ax, 44, 28, r'$x^3-3x+1=0$ : 3 sur 6', 'autre', 's')
for i in range(6):
    box(ax, 6 + i * 13, 16, 11, 9, 'autre', fill=(i < 3), dash=(i >= 3))
text(ax, 44, 7, 'pointillé : permutation absente du groupe', 'fixe', 's')
save(fig, '65-100')
