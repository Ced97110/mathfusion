import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [(r'$\arcsin(1/2)$', r'$\pi/6$ (30°)'), (r'$\arcsin 1$', r'$\pi/2$ (90°)'), (r'$\arcsin(-1/2)$', r'$-\pi/6$ (−30°)'),
        (r'$\arccos(-1/2)$', r'$2\pi/3$ (120°)'), (r'$\arccos(-1)$', r'$\pi$ (180°)'),
        (r'$\arctan\sqrt{3}$', r'$\pi/3$ (60°)'), (r'$\arctan(-1)$', r'$-\pi/4$ (−45°)')]
for i, (a, b) in enumerate(rows):
    y = 74 - i * 11
    box(ax, 4, y, 36, 9, 'sujet', label=a, size='s')
    arrow(ax, (41.5, y + 4.5), (46.5, y + 4.5), 'fixe')
    box(ax, 48, y, 36, 9, 'resultat', label=b, size='s')
save(fig, '33-099')
