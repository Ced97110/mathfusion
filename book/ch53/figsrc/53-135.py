import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
# p, q donnent n et phi
box(ax, 2, 54, 20, 10, 'autre', label='p = 23', size='s')
box(ax, 24, 54, 20, 10, 'autre', label='q = 29', size='s')
arrow(ax, (46, 59), (52, 59), 'varie')
box(ax, 53, 54, 16, 10, 'sujet', label='n = 667', size='s')
box(ax, 70, 54, 16, 10, 'autre', label='φ = 616', size='s')
# e et d sont deux nombres de 0 à 616
f = numberline(ax, 6, 76, 34, 0, 616, step=616, arrow_right=False)
disc(ax, f(487), 34, 1.7, 'sujet'); disc(ax, f(191), 34, 1.7, 'autre')
text(ax, f(487), 40, 'e = 487', 'sujet', 's')
text(ax, f(191), 40, 'd = 191', 'autre', 's')
text(ax, 44, 22, '487 × 191 = 1 + 151 × 616', 'resultat', 's')
# message 25 -> 169 -> 25
box(ax, 4, 3, 18, 9, 'sujet', label='25')
box(ax, 35, 3, 18, 9, 'varie', label='169')
box(ax, 66, 3, 18, 9, 'resultat', label='25')
arrow(ax, (23, 7.5), (34, 7.5), 'sujet'); arrow(ax, (54, 7.5), (65, 7.5), 'autre')
save(fig, '53-135')
