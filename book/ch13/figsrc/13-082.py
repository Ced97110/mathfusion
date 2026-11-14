import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, 'deux signes −, produit +', 'resultat', 'm')
box(ax, 3, 24, 52, 12, 'resultat', label='(−8) × (−6) = 48', size='l')
box(ax, 59, 24, 26, 12, 'sujet', label='− et −', size='m')
box(ax, 3, 5, 52, 12, 'autre', label='(−8) × 6 = −48', size='l')
box(ax, 59, 5, 26, 12, 'autre', label='− et +', size='m')
save(fig, '13-082')
