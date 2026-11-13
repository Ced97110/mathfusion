import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 8, 57.5, 16, 9, 'fixe', label=r'$a$')
box(ax, 28, 57.5, 30, 9, 'varie', label=r'$p$')
box(ax, 62, 57.5, 16, 9, 'fixe', label=r'$b$')
line(ax, [(4, 52.5), (84, 52.5)], 'fixe', dash=True)
text(ax, 44, 47, 'p tient la place de :', 'varie', 'm')
for y, a, p, b in [(36, '3', '+', '5'), (23, 'α', '∘', 'β'), (10, 'ab', 'bout à bout', 'ba')]:
    box(ax, 8, y - 4.5, 16, 9, 'sujet', label=a)
    box(ax, 28, y - 4.5, 30, 9, 'varie', label=p)
    box(ax, 62, y - 4.5, 16, 9, 'sujet', label=b)
save(fig, '44-056')
