import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 2, 4, 84, 40, 'fixe', fill=False, dash=True); text(ax, 44, 49, r'$\mathbb{Q}$ : un ensemble de paquets', 'encre', 'm')
box(ax, 5, 8, 52, 26, 'sujet')
for i, s in enumerate([r'$\frac{3}{4}$', r'$\frac{6}{8}$', r'$\frac{9}{12}$']): text(ax, 15 + i * 16, 21, s, 'sujet', 'l')
text(ax, 31, 12, 'une fraction = un paquet', 'sujet', 's')
box(ax, 61, 8, 22, 26, 'autre'); text(ax, 72, 21, r'$\frac{5}{6}$', 'autre', 'l'); text(ax, 72, 12, 'un autre paquet', 'autre', 's')
save(fig, '43-080')
