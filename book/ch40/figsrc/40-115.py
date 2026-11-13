import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 25, 84, 'rectangulaire', 'autre', 'm', weight='bold')
text(ax, 25, 80, '6 lignes', 'autre', 's')
text(ax, 68, 84, 'polaire', 'sujet', 'm', weight='bold')
text(ax, 68, 80, '1 ligne', 'sujet', 's')
rows = ['A = x² + y² + c² = 1,5', 'A² = 2,25', '4c²x² = 4 × 0,5 × 1 = 2',
        'A² − 4c²x² = 0,25', 'c⁴ = 0,5² = 0,25', 'égaux : c’est sur la courbe']
for i, s in enumerate(rows):
    box(ax, 3, 68 - i * 11, 44, 9, 'autre', label=s, size='s')
box(ax, 52, 68, 34, 9, 'sujet', label=r'$r^2=2\times 0{,}5\times\cos 0=1$', size='s')
text(ax, 69, 61, r'$2c^2\cos 2\theta$ avec $\theta=0$', 'sujet', 's')
text(ax, 44, 4, 'même point : le sommet (1 ; 0)', 'encre', 's')
save(fig, '40-115')
