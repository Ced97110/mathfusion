import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u, x0 = 2.5, 8
text(ax, 40, 60, '23 + 3 = 26 = 1 × 26 + 0', 'encre', 'm')
box(ax, x0, 46, 23 * u, 8, 'sujet', label='23')
box(ax, x0 + 23 * u, 46, 3 * u, 8, 'varie', label='3', r=0.5)
text(ax, 40, 40, 'reste 0 : case A', 'resultat', 'm')
text(ax, 40, 35, '29 = 1 × 26 + 3', 'encre', 'm')
box(ax, x0, 22, 26 * u, 8, 'fixe', label='26 : un tour')
box(ax, x0 + 26 * u, 22, 3 * u, 8, 'varie', label='3', r=0.5)
text(ax, 40, 14, 'reste 3 : case D', 'resultat', 'm')
line(ax, [(x0 + 26 * u, 20), (x0 + 26 * u, 56)], 'fixe', dash=True)
save(fig, '53-017')
