import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 1.6
x0 = 6
brace(ax, x0, x0 + 30 * u, 43, 'sujet', r'$x = 30$', down=False)
box(ax, x0, 31, 20 * u, 8, 'sujet', label='20')
box(ax, x0 + 20 * u, 31, 10 * u, 8, 'varie', label='−10')
text(ax, 70, 35, r'$x - 10 = 20$', 'resultat', 's')
box(ax, x0, 14, 10 * u, 8, 'sujet', label='10')
box(ax, x0 + 10 * u, 14, 20 * u, 8, 'limite', fill=False, dash=True, label='manque 20', size='s')
box(ax, x0, 3, 30 * u, 8, 'varie', label='−30')
text(ax, 70, 18, r'$10 - x = -20$', 'limite', 's')
save(fig, '16-101')
