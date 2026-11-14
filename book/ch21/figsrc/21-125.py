import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
rows = [(r'$\frac{1}{6}$', r'$2x$'), (r'$\frac{1}{4}$', r'$3x$'), (r'$\frac{1}{x}$', r'$12$')]
for i, (a, b) in enumerate(rows):
    y = 54 - i * 14
    box(ax, 4, y, 20, 11, 'sujet', label=a, size='m')
    arrow(ax, (26, y + 5.5), (58, y + 5.5), 'varie')
    text(ax, 42, y + 9.5, r'$\times 12x$', 'varie', 's')
    box(ax, 62, y, 22, 11, 'fixe', label=b, size='m')
box(ax, 2, 6, 28, 10, 'fixe', label=r'$2x+3x=12$', size='s')
arrow(ax, (32, 11), (38, 11), 'varie')
box(ax, 40, 6, 18, 10, 'fixe', label=r'$5x=12$', size='s')
arrow(ax, (60, 11), (66, 11), 'varie')
box(ax, 68, 6, 18, 10, 'resultat', label=r'$x=2{,}4$', size='s')
text(ax, 77, 1.8, 'heures', 'resultat', 's')
save(fig, '21-125')
