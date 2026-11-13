import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
u = 1.2
x0 = 6
text(ax, x0, 41, 'vingt retiré d’un nombre', 'encre', 's', ha='left')
box(ax, x0, 30, 30 * u, 8, 'sujet', label='30')
box(ax, x0 + 30 * u, 30, 20 * u, 8, 'varie', label='−20')
text(ax, 77, 34, r'$x - 20$', 'sujet', 'm')
text(ax, x0, 25, 'dix de moins qu’un nombre', 'encre', 's', ha='left')
box(ax, x0, 14, 40 * u, 8, 'sujet', label='40')
box(ax, x0 + 40 * u, 14, 10 * u, 8, 'varie', label='−10')
text(ax, 77, 18, r'$x - 10$', 'sujet', 'm')
brace(ax, x0, x0 + 50 * u, 12, 'sujet', 'départ : le nombre, 50')
save(fig, '16-102')
