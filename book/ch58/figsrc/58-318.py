import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# ligne 1 : torsion dans ℤ/2ℤ
box(ax, 2, 50, 84, 22, 'sujet', fill=True)
text(ax, 6, 69.2, 'torsion : dans ℤ/2ℤ', 'sujet', 's', ha='left', weight='bold')
disc(ax, 14, 56, 3.2, 'fixe', label='0', size='s')
disc(ax, 30, 56, 3.2, 'sujet', label='1', size='s')
arrow(ax, (30, 59.5), (14, 59.5), 'varie', curve=0.5)
text(ax, 22, 64.6, '× 2', 'varie', 's')
text(ax, 38, 59, 'a = 2 ≠ 0, x = 1 ≠ 0', 'sujet', 's', ha='left')
text(ax, 38, 53.5, 'et 2 × 1 = 0', 'sujet', 's', ha='left')
# ligne 2 : pas de torsion dans ℤ²
box(ax, 2, 26, 84, 20, 'autre', fill=True)
text(ax, 6, 42, 'pas de torsion : dans ℤ²', 'autre', 's', ha='left', weight='bold')
text(ax, 6, 33, '2 × (3, 5) = (6, 10)', 'autre', 's', ha='left')
text(ax, 50, 33, '≠ 0 : jamais annulé', 'autre', 's', ha='left')
# ligne 3 : multiplier par 0
box(ax, 2, 2, 84, 20, 'fixe', fill=True)
text(ax, 6, 18, 'ne compte pas : a = 0', 'fixe', 's', ha='left', weight='bold')
text(ax, 6, 9, '0 × x = 0, pour tout x', 'fixe', 's', ha='left')
text(ax, 50, 9, 'on n’apprend rien', 'fixe', 's', ha='left')
save(fig, '58-318')
