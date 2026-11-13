import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, 'inverse de 2 : un nombre × 2 = 1', 'encre', 'm')
rows = [('ℚ', r'$2\times\frac{1}{2}=1$', 'resultat', 'corps'), ('ℝ', r'$2\times\frac{1}{2}=1$', 'resultat', 'corps'),
        ('ℂ', r'$2\times\frac{1}{2}=1$', 'resultat', 'corps'), ('ℤ', r'$2\times ?=1$', 'limite', 'pas un corps')]
for i, (n, e, role, v) in enumerate(rows):
    y = 46 - i * 13
    box(ax, 3, y, 14, 10, 'sujet' if role == 'resultat' else 'limite', label=n, size='l', weight='bold')
    box(ax, 21, y, 36, 10, role, label=e)
    text(ax, 60, y + 5, v, role, 's', ha='left')
text(ax, 44, 2.5, 'aucun entier × 2 ne donne 1', 'limite', 's')
save(fig, '51-114')
