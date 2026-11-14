import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# ligne 1 : M = tor M
text(ax, 2, 52, 'ℤ/12', 'encre', 'm', ha='left')
box(ax, 28, 45, 38, 14, 'sujet', label='M = tor M')
text(ax, 69, 52, 'de torsion', 'sujet', 'm', ha='left', weight='bold')
# ligne 2 : mixte
text(ax, 2, 30, 'ℤ × ℤ/4', 'encre', 'm', ha='left')
box(ax, 28, 23, 38, 14, 'fixe')
box(ax, 30, 25, 12, 10, 'sujet', label='tor M', size='s')
text(ax, 56, 30, 'M', 'fixe', 'm')
text(ax, 69, 30, 'mixte', 'fixe', 'm', ha='left')
# ligne 3 : libre
text(ax, 2, 8, 'ℤ', 'encre', 'm', ha='left')
box(ax, 28, 1, 38, 14, 'fixe')
box(ax, 30, 3, 8, 10, 'sujet', label='0', size='s', r=0.4)
text(ax, 56, 8, 'M', 'fixe', 'm')
text(ax, 69, 8, 'libre', 'fixe', 'm', ha='left')
save(fig, '60-040')
