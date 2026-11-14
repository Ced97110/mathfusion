import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
rows = [('horloge', r'$x+y$', 'sujet'), ('rotations', r'$x\circ y$', 'autre'), ('autre groupe', r'$x\cdot y$', 'fixe')]
for i, (n, s, role) in enumerate(rows):
    y = 38 - 16 * i
    text(ax, 14, y + 4, n, role, 's')
    box(ax, 27, y - 1, 20, 10, role, label=s)
    arrow(ax, (48, y + 4), (58, 24 + 4 * (1 - i) + 0), 'varie')
box(ax, 59, 17, 24, 16, 'resultat', label=r'$xy$', size='xl')
text(ax, 71, 11, r'$x$ combiné à $y$', 'resultat', 's')
save(fig, '45-021')
