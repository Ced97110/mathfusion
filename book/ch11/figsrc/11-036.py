import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 2, 56, 14, 12, 'sujet', label=r'$k$', size='l')
text(ax, 9, 52.5, 'kilo', 'sujet', 's')
text(ax, 21, 62, '=', 'encre', 'l')
box(ax, 26, 56, 24, 12, 'resultat', label='1 000', size='l')
text(ax, 55, 62, '=', 'encre', 'l')
box(ax, 60, 56, 26, 12, 'resultat', label=r'$10^{3}$', size='l')
text(ax, 73, 52.5, r'$10 \times 10 \times 10$', 'resultat', 's')
for i in range(3):
    box(ax, 2 + i * 28.5, 24, 27, 12, 'autre', label='1 000 m')
brace(ax, 2, 85.5, 22, 'varie', '3 km = 3 × 1 000 m = 3 000 m')
save(fig, '11-036')
