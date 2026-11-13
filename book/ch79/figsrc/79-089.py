import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 2, 64, 84, 13, 'sujet', label=r'On pose : $a\leq b$ si $a\vee b=b$', size='l', weight='bold')
text(ax, 44, 58.5, 'avec seulement PPCM et PGCD', 'fixe', 's')
rows = [(38, 'PPCM(4, 12) = 12', r'$4\leq12$ : vrai', 'resultat', '4 divise 12'),
        (14, 'PPCM(12, 20) = 60', r'$12\leq20$ : faux', 'limite', '12 ne divise\npas 20')]
for y, c, d, role, e in rows:
    box(ax, 1, y, 29, 12, 'fixe', label=c, size='s'); box(ax, 35, y, 24, 12, role, label=d, size='s'); box(ax, 64, y, 22, 12, role, label=e, size='s')
    arrow(ax, (30.5, y + 6), (34.5, y + 6), 'varie'); arrow(ax, (59.5, y + 6), (63.5, y + 6), 'varie')
text(ax, 44, 5, 'on retrouve la divisibilité', 'resultat', 's')
save(fig, '79-089')
