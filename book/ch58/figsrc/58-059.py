import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
f1, f2 = (2, 1), (1, 1)
def comb(a, b): return (a * f1[0] + b * f2[0], a * f1[1] + b * f2[1])
assert comb(1, 3) == (5, 4) and comb(1, 0) == (2, 1) and comb(2, 3) == (7, 5) and comb(3, 0) == (6, 3)
text(ax, 24, 68, r'$M$ : couples, base (2, 1), (1, 1)', 'sujet', 's')
text(ax, 69, 68, r'$R^{(2)}$ : coordonnées', 'autre', 's')
# repères : un élément et ses coordonnées
box(ax, 2, 50, 20, 9, 'sujet', label='(5, 4)', size='s')
box(ax, 58, 50, 20, 9, 'autre', label='(1, 3)', size='s')
arrow(ax, (23, 54.5), (57, 54.5), 'varie', both=True)
text(ax, 40, 58, 'coordonnées', 'varie', 's')
# addition
box(ax, 2, 28, 38, 9, 'sujet', label='(5, 4) + (2, 1) = (7, 5)', size='s')
box(ax, 48, 28, 38, 9, 'autre', label='(1, 3) + (1, 0) = (2, 3)', size='s')
arrow(ax, (41, 32.5), (47, 32.5), 'varie', both=True)
# multiplication
box(ax, 2, 8, 38, 9, 'sujet', label='3 × (2, 1) = (6, 3)', size='s')
box(ax, 48, 8, 38, 9, 'autre', label='3 × (1, 0) = (3, 0)', size='s')
arrow(ax, (41, 12.5), (47, 12.5), 'varie', both=True)
save(fig, '58-059')
