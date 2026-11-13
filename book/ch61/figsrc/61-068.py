import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
disc(ax, 14, 43, 8, 'autre', label=r'$\pi$', size='xl')
text(ax, 14, 28, 'transcendant', 'autre', 's')
text(ax, 14, 24, r'sur $\mathbb{Q}$', 'autre', 's')
text(ax, 56, 80, 'polynôme non nul, en $\\pi$', 'fixe', 's')
rows = [(68, 'degré 1'), (56, 'degré 2'), (44, 'degré 3'), (20, 'degré 1 000')]
for y, lab in rows:
    box(ax, 28, y - 4.5, 30, 9, 'fixe', label=lab, size='s')
    arrow(ax, (58, y), (65, y), 'fixe')
    box(ax, 65, y - 4.5, 19, 9, 'limite', label=r'valeur $\neq 0$', size='s')
    arrow(ax, (22, 43), (28, y), 'autre', lw=0.7)
text(ax, 43, 32, '. . .', 'fixe', 'l')
save(fig, '61-068')
