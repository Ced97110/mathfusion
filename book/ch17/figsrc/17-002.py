import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
text(ax, 22, 48, 'une phrase par distance', 'fixe', 's')
for y, d, p in [(34, 4, 11), (14, 5, 13)]:
    box(ax, 4, y, 36, 9, 'fixe', label=rf'$3 + 2 \times {d} = {p}$', size='s')
    text(ax, 22, y - 3.5, rf'$d = {d}$', 'varie', 's')
    arrow(ax, (41, y + 4.5), (54, 31), 'fixe')
text(ax, 70, 48, 'une écriture', 'sujet', 's')
box(ax, 54, 24, 32, 14, 'sujet', label=r'$3 + 2d$', size='xl')
text(ax, 70, 18, r'$d$ : nombre de km', 'varie', 's')
save(fig, '17-002')
