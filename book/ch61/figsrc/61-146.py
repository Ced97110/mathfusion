import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy = 23, 32
disc(ax, cx, cy, 22, 'limite')
disc(ax, cx, cy, 14, 'resultat')
disc(ax, cx, cy, 6, 'sujet', label='ℚ', size='l')
text(ax, cx, cy + 10, r'$\overline{\mathbb{Q}}$', 'resultat', 'l')
text(ax, cx, cy + 18, 'ℂ', 'limite', 'l')
disc(ax, cx + 12.5, cy - 12.5, 3.2, 'limite', fill=True, label='π', size='m')
Q = r'$\overline{\mathbb{Q}}$'
x = 50
text(ax, x, 50, Q + ' remplit les deux', 'resultat', 's', ha='left')
text(ax, x + 3, 44, '✓ algébriquement clos', 'resultat', 's', ha='left')
text(ax, x + 3, 38, '✓ algébrique sur ℚ', 'resultat', 's', ha='left')
text(ax, x, 26, 'ℂ en échoue une', 'limite', 's', ha='left')
text(ax, x + 3, 20, '✓ algébriquement clos', 'resultat', 's', ha='left')
text(ax, x + 3, 14, '✗ π pas algébrique sur ℚ', 'limite', 's', ha='left')
save(fig, '61-146')
