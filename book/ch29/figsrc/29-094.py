import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)

box(ax, 3, 46, 30, 10, 'varie', label='sin 1 ≈ 0,8415', size='s')
box(ax, 41, 46, 44, 10, 'sujet', label='PN ≈ 3 × 0,8415 ≈ 2,524', size='s')
arrow(ax, (33.3, 51), (40.7, 51), 'encre')
x0 = 13.7
box(ax, x0, 22, 30.3, 8, 'resultat', label='PN ≈ 2,524', size='s')
box(ax, x0 + 30.3, 22, 30.3, 8, 'resultat', label='NQ ≈ 2,524', size='s')
text(ax, x0, 34, r'$P$', 'encre', 'm')
text(ax, x0 + 30.3, 34, r'$N$', 'encre', 'm')
text(ax, x0 + 60.6, 34, r'$Q$', 'encre', 'm')
arrow(ax, (52, 45.7), (30, 30.5), 'sujet')
brace(ax, x0, x0 + 60.6, 22, 'resultat', label='PQ = 2 × PN ≈ 5,05 cm')
save(fig, '29-094')
