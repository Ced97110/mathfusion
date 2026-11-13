import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
a = 22
box(ax, 6, 18, a, a, 'varie', label='aire 2')
line(ax, [(6, 14), (6 + a, 14)], 'varie'); text(ax, 6 + a / 2, 10, r'$d$', 'varie', 'l')
text(ax, 6 + a + 4, 18 + a / 2, r'$d$', 'varie', 'l')
x, w, h = 46, 36, 9
box(ax, x, 38, w, h, 'sujet', label=r'$d\times d = 2$')
box(ax, x, 22, w, h, 'sujet', label=r'$d^2 = 2$')
box(ax, x, 6, w, h, 'resultat', label=r'$d = \sqrt{2}$')
arrow(ax, (x + w / 2, 38), (x + w / 2, 31), 'fixe'); arrow(ax, (x + w / 2, 22), (x + w / 2, 15), 'fixe')
text(ax, 6 + a / 2, 46, 'carré de côté d', 'varie', 's')
save(fig, '22-018')
