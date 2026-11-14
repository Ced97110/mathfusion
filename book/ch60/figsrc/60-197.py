import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 24, 64, 'M = ℤ/2 ⊕ ℤ/2', 'autre', 'm', weight='bold')
text(ax, 66, 64, 'D/(2) = ℤ/2', 'sujet', 'm', weight='bold')
for r in range(2):
    for c in range(2):
        box(ax, 8 + c * 17, 46 - r * 14, 17, 14, 'varie', label='0 ou 1', size='s')
text(ax, 24, 27, '4 cases × 2 choix', 'varie', 's')
text(ax, 24, 20, '16 endomorphismes', 'resultat', 's')
for i, x in enumerate((58, 74)):
    disc(ax, x, 48, 5, 'sujet', label=str(i), size='m')
text(ax, 66, 36, '2 éléments', 'sujet', 's')
text(ax, 44, 11, '16 ≠ 2', 'limite', 'xl', weight='bold')
text(ax, 44, 3, 'plus que des multiplications', 'encre', 's')
save(fig, '60-197')
